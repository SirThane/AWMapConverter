import tile_data
import csv


# Warp tile = 0 or an empty CSV cell

class AWMap:

    def __init__(self, data, source):
        self.data = data
        self.size_w = 0
        self.size_h = 0
        self.style = 0
        self.awmap = []
        self.source = source
        if self.source == "AWS":
            self.bin_data = bytearray(self.data)
            self.from_aws()

    def from_aws(self):
        # Width, Height, and graphic style
        self.size_w, self.size_h, self.style = self.bin_data[10:13]
        self.awmap = [[AWTile(self, x + 1, y + 1, self.terr_from_bin(x, y), self.unit_from_bin(x, y))
                       for y in range(self.size_h)] for x in range(self.size_w)]

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
        return self.awmap[x][y]


class AWTile:  # TODO: Account for multi-tile terrain objects e.g. death ray, volcano, etc.

    def __init__(self, awmap: AWMap, x: int, y: int, terrain=0, unit=0):
        self.x, self.y, self.unit, self.awmap = x, y, unit, awmap
        if self.awmap.source == "AWS":
            self.terr_bin = terrain

    def tile(self, x, y):
        return self.awmap.tile(x, y)

    def mod_terr(self, terrain):
        pass

    def mod_unit(self, unit):
        pass
