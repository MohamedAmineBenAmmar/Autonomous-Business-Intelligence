import atoti as tt
import pandas as pd

class DBES_Cube():
    def __init__(self) -> None:
        self.session = tt.Session()
        
    def get_DBES_table(self):
        df = pd.read_sql_table('DBES', 'postgresql+psycopg2://postgres:postgres@localhost:5432/Autonomous-BI-DWH')  
        self.table = self.session.read_pandas(df, table_name="DBES", keys=["id"])   
        
    def create_cube(self):
        self.cube = self.session.create_cube(self.table)
        l = self.cube.levels
        h = self.cube.hierarchies

        h["Project"] = [l["project_name"], l["project_type"], l["id"]]
        h["Facts"] = [l["facts"]]
        h["Rules"] = [l["rules"]]

        del h["project_name"]
        del h["project_type"]
        del h["facts"]
        del h["rules"] 
        del h["id"]      
        
        