import tile_data
from collections import Iterable
from io import StringIO
import csv
from time import sleep
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

    def from_aws(self):  # TODO: Make sure the coords are right
        # Width, Height, and graphic style
        self.size_w, self.size_h, self.style = self.bin_data[10:13]
        self.map_size = self.size_w * self.size_h  # Number of tiles * 2 due to 2 bytes per tile

        # Chop out the terrain data as a list of ints
        terr_data = [int.from_bytes(self.bin_data[x + 13:x + 15], 'little') for x in
                     range(0, self.map_size * 2, 2)]

        # Chop out the unit data as a list of ints
        unit_data = [int.from_bytes(self.bin_data[x + (self.map_size * 2) + 13:x + (self.map_size * 2) + 15], 'little')
                     for x in range(0, self.map_size * 2, 2)]

        self.map = self.invert_map_axis([[AWTile(self, x, y, self.terr_from_aws(x, y, terr_data),
                                                 self.unit_from_aws(x, y, unit_data))
                                          for y in range(self.size_h)] for x in range(self.size_w)])

        self.title, self.author, self.desc = self.meta_from_aws(self.bin_data[13 + (self.map_size * 4):])

    def invert_map_axis(self, map):
        return [[map[x][y] for x in range(self.size_w)] for y in range(self.size_h)]

    def terr_from_aws(self, x, y, data):
        # Return 2 byte terrain value from binary data for coordinate (x, y)
        offset = y + (x * self.size_h)
        return tile_data.AWS_TERR.get(data[offset], 0)

    def unit_from_aws(self, x, y, data):
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
            return self.map[x][y]
        except IndexError:
            return False

    def to_awbw(self):
        si = StringIO()
        writer = csv.writer(si)
        for row in [[tile.awbw_id for tile in row] for row in self.map]:
            writer.writerow(row)
        return si.getvalue()


class AWTile:  # TODO: Account for multi-tile terrain objects e.g. death ray, volcano, etc.

    def __init__(self, awmap: AWMap, x, y, terr, unit):
        self.x, self.y, self.terr, self.unit, self.awmap = x, y, terr, unit, awmap

    def __repr__(self):
        return f"({self.x + 1}, {self.y + 1}): " \
               f"<{tile_data.MAIN_TERR.get(self.terr, 'Plain')}> " \
               f"<{tile_data.MAIN_UNIT.get(self.unit, 'Empty')}>"

    def tile(self, x, y):
        return self.awmap.tile(x, y)

    @property
    def awbw_id(self):
        return tile_data.MAIN_TERR_TO_AWBW.get(self.terr, 1)[0]

    def mod_terr(self, terrain):
        pass

    def mod_unit(self, unit):
        pass
