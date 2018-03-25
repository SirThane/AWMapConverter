import tile_data
import csv


# Warp tile = 0 or an empty CSV cell
# TODO: Test these
# TODO: Also, implement excepting invalid tile data for AWBW export as Warp tile
# TODO: Guess we'll need to implement excepting invalid tiles for AWS export. Plains?

class AWMap:

    def __init__(self, data, source):
        self.data = data
        self.size_w = 0
        self.size_h = 0
        self.style = 0
        self.map = []
        self.source = source
        self.pass_buffer = []  # Buffer tile coords to skip for multi-tile objects e.g. Volcano, Deathray
        if self.source == "AWS":
            self.bin_data = bytearray(self.data)
            self.from_aws()

    # def __str__(self):  # TODO: Make a string representation of the tile objects.
    #     pass

    def from_aws(self):  # TODO: Make sure the coords are right
        # Width, Height, and graphic style
        self.size_w, self.size_h, self.style = self.bin_data[10:13]
        map_size = self.size_w * self.size_h * 2  # Number of tiles * 2 due to 2 bytes per tile

        # Chop out the terrain data as a list of ints
        terr_data = [int.from_bytes(self.bin_data[x + 13:x + 15], 'little') for x in
                     range(0, map_size, 2)]

        # Chop out the unit data as a list of ints
        unit_data = [int.from_bytes(self.bin_data[x + map_size + 13:x + map_size + 15], 'little') for x in
                     range(0, map_size, 2)]

        self.map = [[AWTile(self, x + 1, y + 1, self.terr_from_bin(x, y), self.unit_from_bin(x, y))
                       for y in range(self.size_h)] for x in range(self.size_w)]

    def find_terr_value(self):
        pass

    def find_unit_value(self):
        pass

    def terr_from_bin(self, x, y):
        # Return 2 byte terrain value from binary data for coordinate (x, y)
        offset = (y + (x * self.size_h)) * 2
        return self.bin_data[offset:offset + 2]

    def unit_from_bin(self, x, y):
        # Return 2 byte unit value from binary data for coordinate (x, y)
        offset = ((y + (x * self.size_h)) * 2) + (self.size_h * self.size_w * 2)
        return self.bin_data[offset:offset + 2]

    def tile(self, x, y):
        # Return tile object at coordinate (x, y)
        return self.map[x][y]


class AWTile:  # TODO: Account for multi-tile terrain objects e.g. death ray, volcano, etc.

    def __init__(self, awmap: AWMap, x: int, y: int, terr: int=0, unit: int=0):
        self.x, self.y, self.terr, self.unit, self.awmap = x, y, terr, unit, awmap

    def __repr__(self):
        return f"({self.x}, {self.y}): " \
               f"<{tile_data.MAIN_TERR.get(self.terr, 'Plain')}>" \
               f"<{tile_data.MAIN_UNIT.get(self.unit, 'Empty')}>"

    def tile(self, x, y):
        return self.awmap.tile(x, y)

    def mod_terr(self, terrain):
        pass

    def mod_unit(self, unit):
        pass
