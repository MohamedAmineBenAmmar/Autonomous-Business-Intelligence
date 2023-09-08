import DWH



dbes_cube = DWH.OLAP.DBES_Cube()
print(dbes_cube.session)

dbes_cube.get_DBES_table()
print(dbes_cube.table)

dbes_cube.create_cube()
print(dbes_cube.cube)

h = dbes_cube.cube.hierarchies
print("h:")
print(h)

l = dbes_cube.cube.levels
print("l:")
print(l)

print( [l["rules"], l["facts"]])




