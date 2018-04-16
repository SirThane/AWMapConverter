from awmap import AWMap


def bread(infile='TestFiles\\key_unit.aws'):
    with open(infile, 'rb') as bin_file:
        return AWMap().from_aws(bin_file.read())


newmap = bread()


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

newmap.minimap.save("TestFiles\\key_unit.gif", save_all=True)
