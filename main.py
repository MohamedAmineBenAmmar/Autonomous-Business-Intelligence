from dotenv import load_dotenv
import DWH

# Load environment variables from .env file
load_dotenv()

# Constructor call and session creation
dbes_cube = DWH.OLAP.DBES_Cube()

# Fetch the SQL table from the data warehouse
dbes_cube.get_DBES_table()

# Create the OLAP cube
dbes_cube.create_cube()

# Get the rules and facts that the expert system needs
# rules = dbes_cube.get_expert_system_rules(("Kyanite", "A", "1"))
# facts = dbes_cube.get_expert_system_facts(("Kyanite", "A", "1"))

kyanite_rules = dbes_cube.get_expert_system_rules(("Kyanite", "A", "1"))
kyanite_facts = dbes_cube.get_expert_system_facts(("Kyanite", "A", "1"))
print("Kyanite project rules: ", kyanite_rules)
print("Kyanite project facts: ", kyanite_facts)

garnet_rules = dbes_cube.get_expert_system_rules(("Garnet", "B", "2"))
garnet_facts = dbes_cube.get_expert_system_facts(("Garnet", "B", "2"))

print("Garnet project rules: ", garnet_rules)
print("Garnet project facts: ", garnet_facts)
