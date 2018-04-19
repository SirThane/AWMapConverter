from awmap import AWMap


def bread(infile='TestFiles\\key_unit.aws'):
    with open(infile, 'rb') as bin_file:
        return AWMap().from_aws(bin_file.read())


# newmap = bread()
newmap = AWMap().from_awbw("""
34,35,34,52,34,35,34
34,24,24,17,24,24,34
110,102,105,16,104,102,108
34,34,114,113,114,34,34
110,102,106,16,103,102,108
34,22,22,17,22,22,34
34,35,34,125,34,35,34
""")

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

# with open("TestFiles\\BHTestWrite.aws", "wb") as out_file:
#     out_file.write(newmap.to_aws)

print("\n", newmap.to_awbw)

# newmap.minimap.save("TestFiles\\csvtest.gif", save_all=True)
