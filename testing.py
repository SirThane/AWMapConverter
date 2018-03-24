

def br(infile='test.aws'):
    with open(infile, 'rb') as bin_file:
        return bin_file.read()


def bra(infile='test.aws'):
    return bytearray(br(infile))


def wr(outfile='test.aws', data: bytes=b'\x00'):
    with open(outfile, 'wb') as bin_file:
        bin_file.write(data)


def find_size(data: bytes):
    return data[10:12]


def find_terr(data: bytes):
    size_bytes = list(find_size(data))
    size = size_bytes[0] * size_bytes[1] * 2

    return [int.from_bytes(data[x + 13:x + 15], 'little') for x in range(0, size, 2)]


def mod_terr(x, y, data: bytes):
    pass


def mod_unit(x, y, data: bytes):
    pass


data = bra()
# print(list(find_size(data)))
# print(data)
print(find_terr(data))
