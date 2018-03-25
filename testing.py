import map
# def br(infile='test.aws'):
#     with open(infile, 'rb') as bin_file:
#         return bin_file.read()
#
#
# def bra(infile='test.aws'):
#     return bytearray(br(infile))
#
#
# def wr(outfile='test.aws', data: bytes=b'\x00'):
#     with open(outfile, 'wb') as bin_file:
#         bin_file.write(data)
#
#
# def find_size(data: bytes):
#     return data[10:12]
#
#
# def find_terr(data: bytes):
#     size_bytes = list(find_size(data))
#     size = size_bytes[0] * size_bytes[1] * 2
#
#     return [int.from_bytes(data[x + 13:x + 15], 'little') for x in range(0, size, 2)]
#
#
# def terr_at_coord(data: bytes, x, y):
#     # Return 2 byte terrain value from binary data for coordinate (x, y)
#     offset = (y + (x * find_size(data))) * 2
#     return data[offset:offset + 2]
#
#
# def find_unit(data: bytes):
#     pass
#
#
# def mod_terr(data: bytes, x, y, unit):
#     pass
#
#
# def mod_unit(data: bytes, x, y, unit):
#     pass
#
#
# def write_terr_data(data: bytes, terr_data: bytes):
#     pass


# print(list(find_size(data)))
# print(data)
# print(find_terr(bra()))

def bread(infile='test.aws'):
    with open(infile, 'rb') as bin_file:
        return map.AWMap(bin_file.read(), "AWS")


print(bread())
