import map


def bread(infile='test.aws'):
    with open(infile, 'rb') as bin_file:
        return map.AWMap(bin_file.read(), "AWS")


awmap = bread('key_terr.aws')
with open(f"{awmap.title}.txt", 'w') as outfile:
    outfile.write(awmap.to_awbw())

print(bread().to_awbw())
