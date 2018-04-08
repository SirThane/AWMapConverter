import tile_data
from collections import Iterable
from math import cos, sin, pi, trunc
# from time import sleep


# Warp tile = 0 or an empty CSV cell
# TODO: Test these

# TODO: Also, implement excepting invalid tile data for AWBW export as Warp tile
# TODO: Guess we'll need to implement excepting invalid tiles for AWS export. Plains?


def flatten(items):
    """Yield items from any nested iterable; see REF."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


class AWMap:

    def __init__(self, data, source):
        self.data = data
        self.map = []
        self.size_w = 0
        self.size_h = 0
        self.map_size = 0
        self.style = 0
        self.title = None
        self.author = None
        self.desc = None
        self.source = source
        self.pass_buffer = []  # Buffer tile coords to skip for multi-tile objects e.g. Volcano, Deathray
        if self.source == "AWS":
            self.bin_data = bytearray(self.data)
            self.from_aws()

    def __repr__(self):
        nl = "\n"
        return f"{'Map Title: {0}{1}'.format(self.title, nl) if self.title is not None else ''}" \
               f"{'Map Author: {0}{1}'.format(self.author, nl) if self.author is not None else ''}" \
               f"{'Map Description: {0}{1}'.format(self.desc, nl) if self.desc is not None else ''}\n" \
               f"{'{0}'.format(nl).join([str(x) for x in flatten(self.map)])}"

    def __iter__(self):
        for y in range(self.size_h):
            for x in range(self.size_w):
                yield self.tile(x, y)

    def from_aws(self):
        # Width, Height, and graphic style
        self.size_w, self.size_h, self.style = self.bin_data[10:13]
        self.map_size = self.size_w * self.size_h

        # Chop out the terrain data as a list of ints
        terr_data = [int.from_bytes(self.bin_data[x + 13:x + 15], 'little') for x in
                     range(0, self.map_size * 2, 2)]

        # Chop out the unit data as a list of ints
        unit_data = [int.from_bytes(self.bin_data[x + (self.map_size * 2) + 13:x + (self.map_size * 2) + 15], 'little')
                     for x in range(0, self.map_size * 2, 2)]

        map_data = {x: {y: AWTile(self, x, y, self.terr_from_aws(x, y, terr_data), self.unit_from_aws(x, y, unit_data))
                        for y in range(self.size_h)} for x in range(self.size_w)}

        self.map = self.correct_map_axis(map_data)

        self.title, self.author, self.desc = self.meta_from_aws(self.bin_data[13 + (self.map_size * 4):])

    def correct_map_axis(self, inverted_map):
        return {y: {x: inverted_map[x][y] for x in range(self.size_w)} for y in range(self.size_h)}

    def terr_from_aws(self, x, y, data):  # TODO: Correct for country consolidation
        # Return 2 byte terrain value from binary data for coordinate (x, y)
        offset = y + (x * self.size_h)
        return tile_data.AWS_TERR.get(data[offset], 0)

    def unit_from_aws(self, x, y, data):  # TODO: Correct for country consolidation
        # Return 2 byte unit value from binary data for coordinate (x, y)
        offset = y + (x * self.size_h)
        return tile_data.AWS_UNIT.get(data[offset], 0)

    def meta_from_aws(self, data):
        t_size = int.from_bytes(data[:4], 'little')
        a_size = int.from_bytes(data[t_size + 4:t_size + 8], 'little')
        d_size = int.from_bytes(data[t_size + a_size + 8:t_size + a_size + 12], 'little')

        title = data[4:4 + t_size].decode('utf-8')
        author = data[8 + t_size:8 + t_size + a_size].decode('utf-8')
        desc = data[12 + t_size + a_size:12 + t_size + a_size + d_size].decode('utf-8')
        return title, author, desc

    def tile(self, x, y):
        # Return tile object at coordinate (x, y)
        try:
            tile = self.map[y][x]
            try:
                assert tile.x == x
                assert tile.y == y
                return tile
            except AssertionError:
                print(f"Received tile from index with differing coordinates\n"
                      f"Requested:     ({x}, {y})\n"
                      f"Tile Property: ({tile.x}, {tile.y})\n"
                      f"Tile Contents: (T: {tile.terr}, U: {tile.unit})")
                return tile
        except KeyError:
            return AWTile(self, x, y, 999, 0)
            # return False

    def to_awbw(self):
        # si = StringIO()
        # writer = csv.writer(si)
        # for row in [[tile.awbw_id for tile in row] for row in self.map]:
        #     writer.writerow(row)
        # return si.getvalue()

        return '\n'.join(
            [','.join([str(self.tile(x, y).awbw_id) for x in range(self.size_w)]) for y in range(self.size_h)])


class AWTile:  # TODO: Account for multi-tile terrain objects e.g. death ray, volcano, etc.

    def __init__(self, awmap: AWMap, x=0, y=0, terr=0, unit=0):
        self.x, self.y, self.terr, self.unit, self.awmap = x, y, terr, unit, awmap
        self.awareness_override = None

    def __repr__(self):
        return f"({self.x + 1}, {self.y + 1}): " \
               f"<{tile_data.MAIN_TERR.get(self.terr, 'Plain')}> " \
               f"<{tile_data.MAIN_UNIT.get(self.unit, 'Empty')}>"

    def tile(self, x, y):
        """ Grab the AWTile object from AWMap using AWMap.tile()"""
        return self.awmap.tile(x, y)

    @property
    def terr_name(self):
        return tile_data.MAIN_TERR.get(self.terr, "InvalidTerrID")

    @property
    def awbw_id(self):  # TODO fix this and fix the dict
        try:
            return tile_data.MAIN_TERR_TO_AWBW.get(self.terr, 1)[self.awbw_awareness]
        except IndexError:
            return ""

    @property
    def awbw_awareness(self):
        if self.terr in tile_data.MAIN_TERR_TO_AWBW_AWARENESS.keys():
            mask = 0
            for tile in tile_data.MAIN_TERR_TO_AWBW_AWARENESS["aware_of"][self.terr]:
                mask = mask | self.adj_match(tile)
            return tile_data.MAIN_TERR_TO_AWBW_AWARENESS[self.terr][mask]
        else:
            return 0

    def adj_match(self, terr=None):
        if not terr:
            terr = self.terr

        awareness_mask = 0  # #                  West   South    East    North        W  S  E  N
        for i in range(4):  # Below generates [(-1, 0), (0, 1), (1, 0), (0, -1)] for [0, 1, 2, 3]
            if self.tile(self.x - trunc(sin(pi * (i + 1)/2)), self.y - trunc(cos(pi * (i + 1)/2))).terr == terr:
                awareness_mask += 2 ** i

        return awareness_mask

    def mod_terr(self, terr):
        self.terr = terr

    def mod_unit(self, unit):
        self.unit = unit
