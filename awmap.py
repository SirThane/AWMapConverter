try:
    import tile_data
    import minimap
except ImportError:  # Relative Path hackfix for including in other projects.
    from . import tile_data, minimap

from math import cos, sin, pi, trunc
from bs4 import BeautifulSoup as bs

import csv
import requests


# Warp tile = 0 or an empty CSV cell
# TODO: Test these

# TODO: Also, implement excepting invalid tile data for AWBW export as Warp tile
# TODO: Guess we'll need to implement excepting invalid tiles for AWS export. Plains?


# def flatten(items):
#     """Yield items from any nested iterable; see REF."""
#     for x in items:
#         if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
#             yield from flatten(x)
#         else:
#             yield x


class AWMap:

    def __init__(self):
        self.raw_data = None
        self.map = {}
        self.size_w = 0
        self.size_h = 0
        self.map_size = 0
        self.style = 0
        self.title = ""
        self.author = ""
        self.desc = ""
        self.pass_buffer = []  # Buffer tile coords to skip for multi-tile objects e.g. Volcano, Deathray  # TODO

        # Params used from outside class instance
        self.awbw_id = ""
        self.override_awareness = True
        self.nyv = False

        self.countries = []
        self.custom_countries = []
        self.country_conversion = dict()

    def __repr__(self):
        nl = "\n"
        return f"{'Map Title: {0}{1}'.format(self.title, nl) if self.title is not None else ''}" \
               f"{'Map Author: {0}{1}'.format(self.author, nl) if self.author is not None else ''}" \
               f"{'Map Description: {0}{1}'.format(self.desc, nl) if self.desc is not None else ''}\n" \
               f"{'{0}'.format(nl.join([str(x) for x in list(self)]))}"

    def __str__(self):
        return self.__repr__()

    def __iter__(self):
        for y in range(self.size_h):
            for x in range(self.size_w):
                yield self.tile(x, y)

    """
        # Opening File Methods #
    """

    def from_aws(self, data):
        self.raw_data = bytearray(data)

        # Width, Height, and graphic style
        self.size_w, self.size_h, self.style = self.raw_data[10:13]
        self.map_size = self.size_w * self.size_h

        # Chop out the terrain data as a list of ints
        terr_data = [int.from_bytes(self.raw_data[x + 13:x + 15], 'little') for x in
                     range(0, self.map_size * 2, 2)]

        # Chop out the unit data as a list of ints
        unit_data = [int.from_bytes(self.raw_data[x + (self.map_size * 2) + 13:x + (self.map_size * 2) + 15], 'little')
                     for x in range(0, self.map_size * 2, 2)]

        map_data = {x: {y: AWTile(self, x, y, self.terr_from_aws(x, y, terr_data), self.unit_from_aws(x, y, unit_data))
                        for y in range(self.size_h)} for x in range(self.size_w)}

        self.map = self.correct_map_axis(map_data)

        self.title, self.author, self.desc = self.meta_from_aws(self.raw_data[13 + (self.map_size * 4):])

        return self

    def correct_map_axis(self, inverted_map):
        return {y: {x: inverted_map[x][y] for x in range(self.size_w)} for y in range(self.size_h)}

    def from_awbw(self, data="", title="", awbw_id=None):
        self.raw_data = data

        if awbw_id:
            payload = {
                "maps_id": awbw_id
            }
            r_prev = requests.get("http://awbw.amarriner.com/prevmaps.php", params=payload)
            s_prev = bs(r_prev.text, 'html.parser')
            r_text = requests.get("http://awbw.amarriner.com/text_map.php", params=payload)
            s_text = bs(r_text.text, 'html.parser')

            title_href = s_text.find_all("a", href=f"prevmaps.php?maps_id={awbw_id}")

            # Will not be a title if Invalid Map
            if len(title_href) == 0:
                return

            # Cut the CSV text map out of the text_map.php page
            map_table = s_text.find_all("td", "menu")[0].find_next("table").find_next("table").find_all_next("td")
            map_csv = "\n".join([t.contents[0] for t in map_table])

            # Catch AssertionError if not all map rows are same length
            try:
                self._parse_awbw_csv(map_csv)
            except AssertionError:
                return

            # Find exact location of map image on page (top, left
            divmap = s_prev.find(id="map")
            map_style = divmap.find(id="mapImage").get("style").replace(";", "").split(" ")
            map_style = {x: y for x, y in [z.split(':') for z in map_style]}
            origin = {x: int(y.replace("px", "")) for x, y in map_style.items() if x in ["top", "left"]}

            # Find all unit sprites and mod them into the map
            sprites = divmap.find_all("img")[1:]
            if sprites:
                for sprite in sprites:
                    main_id = tile_data.AWBW_UNIT_SPRITE.get(sprite.get("src").split("/")[-1])
                    if main_id:
                        sprite_style = sprite.parent.get("style").replace(";", "").split(" ")[:2]
                        sprite_style = {x: y for x, y in [z.split(':') for z in sprite_style]}
                        coords = {x: int(y.replace("px", "")) for x, y in sprite_style.items() if x in ["top", "left"]}
                        coords = {
                            "x": (coords["left"] - origin["left"]) // 16,
                            "y": (coords["top"] - origin["top"]) // 16,
                        }
                        self.tile(**coords).mod_unit(main_id)

            # Add the map meta data
            author = s_prev.find_all("td", "menu")[0].next_sibling.span.a.contents
            if author:
                self.author = author[0]
            self.title = title_href[0].contents[0]
            self.awbw_id = str(awbw_id)
            self.desc = r_prev.url

            return self

        elif data:
            try:
                self._parse_awbw_csv(data)
            except AssertionError:
                return

            self.title = title if title else "[Untitled]"

            return self

        return

    def _parse_awbw_csv(self, data):
        csv_map = [*csv.reader(data.strip('\n').split('\n'))]

        # Make sure all rows passed are equal length
        # Calling method will need to catch AssertionError
        assert all(map(lambda r: len(r) == len(csv_map[0]), csv_map))

        self.size_h, self.size_w = len(csv_map), len(csv_map[0])

        for y in range(self.size_h):
            self.map[y] = {}
            for x in range(self.size_w):
                self.map[y][x] = AWTile(self, x, y, **self.terr_from_awbw(csv_map[y][x]))

    def terr_from_aws(self, x, y, data):  # TODO: Correct for country consolidation
        # Return 2 byte terrain value from binary data for coordinate (x, y)
        offset = y + (x * self.size_h)
        return tile_data.AWS_TERR.get(data[offset], 0)

    def unit_from_aws(self, x, y, data):  # TODO: Correct for country consolidation
        # Return 2 byte unit value from binary data for coordinate (x, y)
        offset = y + (x * self.size_h)
        return tile_data.AWS_UNIT.get(data[offset], 0)

    def meta_from_aws(self, data):  # TODO: This needs refactoring. Can be optimized.
        t_size = int.from_bytes(data[:4], 'little')
        a_size = int.from_bytes(data[t_size + 4:t_size + 8], 'little')
        d_size = int.from_bytes(data[t_size + a_size + 8:t_size + a_size + 12], 'little')

        title = data[4:4 + t_size].decode('utf-8')
        author = data[8 + t_size:8 + t_size + a_size].decode('utf-8')
        desc = data[12 + t_size + a_size:12 + t_size + a_size + d_size].decode('utf-8')
        return title, author, desc

    def terr_from_awbw(self, terr):
        terr = int(terr)
        main_id = tile_data.AWBW_TERR.get(terr, 1)
        if main_id in tile_data.MAIN_TERR_TO_AWBW_AWARENESS["aware_of"].keys():
            offset = terr - tile_data.MAIN_TERR_TO_AWBW.get(main_id)[0]
            _awareness = tile_data.MAIN_TERR_TO_AWBW_AWARENESS[main_id]
            override = list(_awareness.keys())[list(_awareness.values()).index(offset)]
            return {"terr": main_id, "awareness_override": override}
        else:
            return {"terr": main_id}

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

    @property
    def to_awbw(self):
        return '\n'.join(  # String cat with list comps was just way easier than dealing with csv and StringIO
            [','.join([str(self.tile(x, y).awbw_id) for x in range(self.size_w)]) for y in range(self.size_h)])

    @property
    def to_aws(self):
        ret = bytearray(b'AWSMap001') + b'\x00'

        style = self.style if self.style else 5

        for b in [m.to_bytes(1, 'little') for m in [self.size_w, self.size_h, style]]:
            ret += b
        for b in [terr.to_bytes(2, 'little') for terr in
                  [self.tile(x, y).aws_terr_id for x in range(self.size_w) for y in range(self.size_h)]]:
            ret += b
        for b in [unit.to_bytes(2, 'little') for unit in
                  [self.tile(x, y).aws_unit_id for x in range(self.size_w) for y in range(self.size_h)]]:
            ret += b

        ret += len(self.title).to_bytes(4, 'little') + self.title.encode('utf-8')
        ret += len(self.author).to_bytes(4, 'little') + self.author.encode('utf-8')
        ret += len(self.desc).to_bytes(4, 'little') + self.desc.encode('utf-8')

        return ret

    @property
    def minimap(self):
        return minimap.AWMinimap(self).map


class AWTile:  # TODO: Account for multi-tile terrain objects e.g. death ray, volcano, etc.

    def __init__(self, awmap: AWMap, x=0, y=0, terr=0, unit=0, awareness_override=0):
        self.x, self.y, self.terr, self.unit, self.awmap = x, y, terr, unit, awmap
        self.awareness_override = awareness_override

    def __repr__(self):
        return f"({self.x + 1}, {self.y + 1}): " \
               f"<{self.terr}:{tile_data.MAIN_TERR.get(self.terr, 'Plain')}> " \
               f"<{self.unit}:{tile_data.MAIN_UNIT.get(self.unit, 'Empty')}>"

    def __str__(self):
        return self.__repr__()

    def tile(self, x, y):
        """ Grab the AWTile object from AWMap using AWMap.tile()"""
        return self.awmap.tile(x, y)

    @property
    def terr_name(self):
        return tile_data.MAIN_TERR.get(self.terr, "InvalidTerrID")

    @property
    def aws_terr_id(self):
        try:
            return tile_data.MAIN_TERR_TO_AWS.get(self.terr, [1])[0]
        except IndexError:
            return 0

    @property
    def aws_unit_id(self):
        try:
            return tile_data.MAIN_UNIT_TO_AWS.get(self.unit, [65535])[0]
        except IndexError:
            print("IndexError")
            return 65535

    @property
    def awbw_id(self):  # TODO fix this and fix the dict
        terr = tile_data.MAIN_TERR_TO_AWBW.get(self.terr, 1)
        if self.terr in tile_data.MAIN_TERR_TO_AWBW_AWARENESS["aware_of"].keys():
            try:
                return terr[self.awbw_awareness]
            except IndexError:
                return terr[0]
        else:
            return terr[0]

    @property
    def awbw_awareness(self):
        if self.terr in tile_data.MAIN_TERR_TO_AWBW_AWARENESS.keys():
            if self.awmap.override_awareness:
                return tile_data.MAIN_TERR_TO_AWBW_AWARENESS[self.terr][self.awareness_override]
            else:
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
        if terr in tile_data.MAIN_TERR.keys():
            self.terr = terr
        else:
            raise ValueError("Invalid Terrain ID")

    def mod_unit(self, unit):
        if unit in tile_data.MAIN_UNIT.keys():
            self.unit = unit
        else:
            raise ValueError("Invalid Unit ID")
