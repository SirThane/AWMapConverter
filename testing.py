from awmap import AWMap


# def bread(infile='TestFiles\\key_unit.aws'):
#     with open(infile, 'rb') as bin_file:
#         return AWMap().from_aws(bin_file.read())


# newmap = bread()


newmap = AWMap().from_awbw(title="Test", data="""
28,28,28,28,28,28,28,28,28,1,3,44,1,44,28
28,28,1,3,18,15,26,15,22,34,1,1,47,44,28
28,1,1,3,16,3,28,1,16,1,2,1,25,44,28
28,34,34,22,20,28,28,28,25,34,2,34,23,1,28
28,1,1,16,1,28,28,28,25,24,15,24,17,34,28
28,39,22,24,34,28,28,3,16,1,28,28,27,28,28
28,39,42,1,1,1,1,3,3,1,28,30,1,1,28
28,28,39,39,1,1,1,1,1,1,26,1,34,34,28
28,33,28,28,2,34,2,3,35,28,28,28,28,28,28
28,28,28,28,28,28,28,28,28,28,28,28,28,28,28
""")

# newmap = AWMap().from_awbw(awbw_id=74065)


# with open(f"{awmap.title}.txt", 'w') as outfile:
#     outfile.write(awmap.to_awbw())

# print('\n'.join(['\n'.join([f"Coord: {(x, y)} ;; "
#                             f"AWTile:{(awmap.tile(x, y).x, awmap.tile(x, y).y)} ;; "
#                             f"Terr: {awmap.tile(x, y).terr_name}"
#                             for x in range(awmap.size_w)])
#                  for y in range(awmap.size_h)]))

# print(awmap.size_h, awmap.size_w)

# print(awmap.map)

# with open("test.gif", "wb") as out_file:
#     out_file.write(newmap.minimap)

# print(newmap)

with open("TestFiles\\SpangIsland.aws", "wb") as out_file:
    out_file.write(newmap.to_aws)

# print(newmap.to_awbw)

newmap.minimap.save("TestFiles\\SpangIsland.gif", save_all=True)
