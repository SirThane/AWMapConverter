import map


def bread(infile='test.aws'):
    with open(infile, 'rb') as bin_file:
        return map.AWMap(bin_file.read(), "AWS")


awmap = bread()
# with open(f"{awmap.title}.txt", 'w') as outfile:
#     outfile.write(awmap.to_awbw())

# print('\n'.join(['\n'.join([f"Coord: {(x, y)} ;; "
#                             f"AWTile:{(awmap.tile(x, y).x, awmap.tile(x, y).y)} ;; "
#                             f"Terr: {awmap.tile(x, y).terr_name}"
#                             for x in range(awmap.size_w)])
#                  for y in range(awmap.size_h)]))

# print(awmap.size_h, awmap.size_w)

# print(awmap.map)

print(awmap.to_awbw())
