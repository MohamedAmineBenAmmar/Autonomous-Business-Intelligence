import atoti as tt
import pandas as pd
import json
from typing import Tuple

class DBES_Cube():
    def __init__(self) -> None:
        self.session = tt.Session()
        
    def get_DBES_table(self) -> None:
        df = pd.read_sql_table('DBES', 'postgresql+psycopg2://postgres:postgres@localhost:5432/Autonomous-BI-DWH')  
        self.table = self.session.read_pandas(df, table_name="DBES", keys=["project_id"])   
        
    def create_cube(self) -> None:
        self.cube = self.session.create_cube(self.table)
        l = self.cube.levels
        h = self.cube.hierarchies

        h["Project"] = [l["project_name"], l["project_type"], l["project_id"]]
        h["Facts"] = [l["facts"]]
        h["Rules"] = [l["rules"]]

        del h["project_name"]
        del h["project_type"]
        del h["facts"]
        del h["rules"] 
        del h["project_id"]     
        
    def get_expert_system_entity(self, project: Tuple[str, str, str], entity: str) -> str:
        if entity != "facts" and entity != "rules":
            raise ValueError("entity must be either 'facts' or 'rules'")
        
        m = self.cube.measures
        l = self.cube.levels
        h = self.cube.hierarchies
        
        query_df = self.cube.query(
            m["contributors.COUNT"],
            levels=[l[entity], l["project_id"]],
            mode="pretty",
            filter=h["Project"].isin(project)
        )
        
        tmp = query_df.to_dict()
        keys, values = zip(*tmp["contributors.COUNT"].items())
        stringified_entity = keys[0][0]
        return stringified_entity
        
    def get_expert_system_rules(self, project: Tuple[str, str, str]) -> dict:       
        stringified_rules = self.get_expert_system_entity(project, "rules")
        rules = json.loads(stringified_rules)
        return rules
    
    def get_expert_system_facts(self, project: Tuple[str, str, str]) -> dict:
        stringified_facts = self.get_expert_system_entity(project, "facts")       
        facts = json.loads(stringified_facts)
        return facts
        
        
        