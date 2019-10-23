from awmapconverter.awmap import AWMap


# def bread(infile='TestFiles\\SpangIsland.aws'):
#     with open(infile, 'rb') as bin_file:
#         return AWMap().from_aws(bin_file.read())


# newmap = bread()

# newmap = AWMap().from_awbw(title="BlacktileTest", data="""
# 42,1,,,
# 1,,,,
# ,,,,
# ,,,,1
# ,,,1,47
# """)

newmap = AWMap().from_awbw(awbw_id=73487)
# newmap = AWMap().from_awbw(awbw_id=73487)

# with open(f"{awmap.title}.txt", 'w') as outfile:
#     outfile.write(awmap.to_awbw())

# with open("test.gif", "wb") as out_file:
#     out_file.write(newmap.minimap)

# with open("TestFiles\\SpangIsland2.aws", "wb") as out_file:
#     out_file.write(newmap.to_aws)

newmap.minimap.save("TestFiles\\73487.gif", save_all=True)
