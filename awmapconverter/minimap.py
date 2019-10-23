
from io import BytesIO
from PIL import Image, ImageDraw, ImageSequence
from PIL.ImagePalette import ImagePalette
from typing import Union, Tuple, List, TypeVar
from pprint import pprint

# import imageio
# from uuid import uuid4


# TODO: Refactor Sprite IDs and junk into tile_data


AWMap = TypeVar("AWMap")


# class Iterator(ImageSequence.Iterator):
#
#     def __len__(self):
#         _len = 0
#         try:
#             self.im.seek(0)
#             while True:
#                 _ = self.__getitem__(_len)
#                 _len += 1
#         except IndexError:
#             return _len
#
#     def len(self):
#         return self.__len__()
#
#     @property
#     def animated(self):
#         return len(self) > 1
#
#     @property
#     def static(self):
#         return not self.animated


def layer(bitmask: Union[str, int]) -> List[Tuple[int, int]]:
    if isinstance(bitmask, str):
        if bitmask[-2] == "b":
            bitmask = bitmask[::-1]
        bitmask = int(bitmask, 2)
    key = [(x, y) for y in range(4) for x in range(4)]
    return [key[i] for i in range(16) if 2 ** i & bitmask]


PALETTE = {
    "white":    (255, 255, 255),

    "green1":   (168, 240, 80),     # Plain light
    "green2":   (104, 232, 56),     # Plain dark
    "green3":   (88,  200, 16),     # Wood light; GE
    "green4":   (82,  164, 16),     # Wood dark

    "blue1":    (112, 176, 248),    # Shoal
    "blue2":    (56,  120, 248),    # Reef medium
    "blue3":    (88,  104, 248),    # River dark; BM; Sea
    "blue4":    (54,  86,  209),    # CI light
    "blue5":    (20,  43,  135),    # CI dark
    "blue6":    (68,  153, 247),    # River light

    "teal1":    (68,  172, 163),    # TG light
    "teal2":    (10,  89,  82),     # TG dark

    "grey1":    (166, 182, 153),    # JS
    "grey2":    (184, 176, 168),    # Road; Bridge; Silo
    "grey3":    (129, 127, 128),    # GS light
    "grey4":    (86,  92,  114),    # GS dark

    "red1":     (176, 144, 136),    # ~~Pipe; Pipe Seam; Broken Pipe Seam~~ AWBW ONLY
    "red2":     (248, 72,  48),     # OS
    "red3":     (208, 70,  93),     # RF light
    "red4":     (119, 11,  35),     # RF dark

    "pink":     (255, 102, 204),    # PC

    "purple1":  (164, 70,  210),    # PL light
    "purple2":  (110, 25,  153),    # PL dark
    "purple3":  (96,  72,  160),    # BH light
    "purple4":  (79,  48,  112),    # BH dark

    "yellow":   (240, 240, 8),      # YC

    "orange1":  (248, 232, 144),    # Mountain light; Reef light
    "orange2":  (207, 179, 158),    # BD light
    "orange3":  (252, 163, 57),     # AB
    "orange4":  (208, 128, 48),     # Mountain medium; Reef dark; Pipe light
    "orange5":  (147, 82,  50),     # BD dark

    "brown1":   (152, 104, 48),     # Mountain dark; Pipe dark
    "brown2":   (104, 80,  56),     # Borders

    "black":    (0,   0,   0),      # Teleport

    # "BLINK":    [(1,   1,   1),   (64,  64,  64),  (127, 127, 127), (190, 190, 190),
    #              (253, 253, 253), (190, 190, 190), (127, 127, 127), (64,  64,  64)],

    # "BLINK":    [(45,  40,  30),  (81,  76,  65),  (108, 103, 92),  (182, 177, 166),
    #              (238, 233, 233), (182, 177, 166), (108, 103, 92),  (81,  76,  65)],

    "BLINK":    [
        (43,  37,  32),  (79,  69,  60),  (122, 106, 92),  (196, 186, 176),
        (239, 236, 233), (196, 186, 176), (122, 106, 92),  (79,  69,  60)
    ],

    # "blink1":   (45,  40,  30),
    # "blink2":   (81,  76,  65),
    # "blink3":   (108, 103, 92),
    # "blink4":   (182, 177, 166),
    # "blink5":   (238, 233, 233),
}


SPEC = {
    "plain":    [
        {
            "xy":   layer("1111110111110111b0"),
            "fill": PALETTE["green1"]
        },
        {
            "xy":   layer("0000001000001000b0"),
            "fill": PALETTE["green2"]
        }
    ],
    "mountain": [
        {
            "xy":   layer("1111100100000000b0"),
            "fill": PALETTE["green1"]
        },
        {
            "xy":   layer("0000010011001000b0"),
            "fill": PALETTE["orange1"]
        },
        {
            "xy":   layer("0000000000000100b0"),
            "fill": PALETTE["orange4"]
        },
        {
            "xy":   layer("0000001000110011b0"),
            "fill": PALETTE["brown1"]
        }
    ],
    # "wood":     [  # Original cart colors
    #     {
    #         "xy":   layer("1001000000001001b0"),
    #         "fill": PALETTE["green1"]
    #     },
    #     {
    #         "xy":   layer("0110111011000000b0"),
    #         "fill": PALETTE["green2"]
    #     },
    #     {
    #         "xy":   layer("0000000100110110b0"),
    #         "fill": PALETTE["green3"]
    #     }
    # ],
    "wood":     [
        {
            "xy":   layer("1001000000001001b0"),
            "fill": PALETTE["green1"]
        },
        {
            "xy":   layer("0110111011000000b0"),
            "fill": PALETTE["green3"]
        },
        {
            "xy":   layer("0000000100110110b0"),
            "fill": PALETTE["green4"]
        }
    ],
    # "river":    [  # Original cart colors
    #     {
    #         "xy":   layer("1111001111111000b0"),
    #         "fill": PALETTE["blue2"]
    #     },
    #     {
    #         "xy":   layer("0000110000000111b0"),
    #         "fill": PALETTE["blue3"]
    #     }
    # ],
    "river":    [
        {
            "xy":   layer("1111001111111000b0"),
            "fill": PALETTE["blue6"]
        },
        {
            "xy":   layer("0000110000000111b0"),
            "fill": PALETTE["blue3"]
        }
    ],
    "road":     [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": PALETTE["grey2"]
        }
    ],
    "sea":      [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": PALETTE["blue3"]
        }
    ],
    "shoal":    [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": PALETTE["blue1"]
        }
    ],
    "reef":     [
        {
            "xy":   layer("1000001000000000b0"),
            "fill": PALETTE["orange1"]
        },
        {
            "xy":   layer("0000100000100000b0"),
            "fill": PALETTE["orange4"]
        },
        {
            "xy":   layer("0000010010010010b0"),
            "fill": PALETTE["blue1"]
        },
        {
            "xy":   layer("0000000001000001b0"),
            "fill": PALETTE["blue2"]
        },
        {
            "xy":   layer("0111000100001100b0"),
            "fill": PALETTE["blue3"]
        },
    ],
    "pipe":     [
        {
            "xy":   layer("1010010110100101b0"),
            "fill": PALETTE["brown1"]
        },
        {
            "xy":   layer("0101101001011010b0"),
            "fill": PALETTE["orange4"]
        }
    ],
    "silo":     [
        {
            "xy":   layer("1010101010100000b0"),
            "fill": PALETTE["white"]
        },
        {
            "xy":   layer("0100010001000000b0"),
            "fill": PALETTE["grey2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "tele":     [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": PALETTE["black"]
        }
    ],
    "nprop":    [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["white"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "osprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["red2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "bmprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["blue3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "geprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["green3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "ycprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["yellow"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "bhprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["purple3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["purple4"]
        }
    ],
    "rfprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["red2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["red4"]
        }
    ],
    "gsprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["grey3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["grey4"]
        }
    ],
    "bdprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["orange2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["orange5"]
        }
    ],
    "abprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["orange3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "jsprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["grey1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "ciprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["blue4"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["blue5"]
        }
    ],
    "pcprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["pink"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "tgprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["teal1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["teal2"]
        }
    ],
    "plprop":   [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": PALETTE["purple1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": PALETTE["purple2"]
        }
    ],
    # "seam":     [
    #     {
    #         "xy":   [layer("1010010110100101b0")] * 8,
    #         "fill": [PALETTE["brown1"]] * 8
    #     },
    #     {
    #         "xy":   [layer("0101101001011010b0")] * 8,
    #         "fill": PALETTE["BLINK"]
    #     }
    # ],
    "seam":     [  # Changed to static
        {
            "xy":   layer("1010010110100101b0"),
            "fill": PALETTE["brown1"]
        },
        {
            "xy":   layer("0101101001011010b0"),
            "fill": PALETTE["white"]
        }
    ],
    "nhq":      [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["white"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "oshq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["red2"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "bmhq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["blue3"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "gehq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["green3"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "ychq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["yellow"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "bhhq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["purple3"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "rfhq":     [  # ALTERED FROM red2 TO red4 TO AVOID CONFLICT WITH OS
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["red4"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "gshq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["grey3"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "bdhq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["orange2"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "abhq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["orange3"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "jshq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["grey1"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "cihq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["blue4"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "pchq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["pink"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "tghq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["teal1"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "plhq":     [
        {
            "xy":   [layer("0000011001100000b0")] * 8,
            "fill": [PALETTE["purple1"]] * 8
        },
        {
            "xy":   [layer("1111100110011111b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],
    "nunit":    [
        {
            "xy":   layer("0000011001100000b0"),
            "fill": PALETTE["white"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        }
    ],
    "osunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["red2"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "bmunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["blue3"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "geunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["green3"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "ycunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["yellow"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "bhunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["purple3"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["purple4"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "rfunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["red2"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["red4"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "gsunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["grey3"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["grey4"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "bdunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["orange2"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["orange5"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "abunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["orange3"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "jsunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["grey1"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "ciunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["blue4"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["blue5"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "pcunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["pink"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["brown2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "tgunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["teal1"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["teal2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
    "plunit":   [
        {
            "xy":   layer("0000001001100000b0"),
            "fill": PALETTE["purple1"]
        },
        {
            "xy":   layer("0110100110010110b0"),
            "fill": PALETTE["purple2"]
        },
        {
            "xy":   layer("0000010000000000b0"),
            "fill": PALETTE["white"]
        }
    ],
}


STATIC_ID_TO_SPEC = {
    "plain":    [1, 12],
    "mountain": [3],
    "wood":     [2],
    "river":    [9],
    "road":     [4, 5],
    "sea":      [6],
    "shoal":    [7],
    "reef":     [8],
    "pipe":     [10],
    "seam":     [11],
    "silo":     [13, 14],
    "tele":     [999],  # TODO
    "nprop":    [102, 103, 104, 105, 106],
    "osprop":   [112, 113, 114, 115, 116],
    "bmprop":   [122, 123, 124, 125, 126],
    "geprop":   [132, 133, 134, 135, 136],
    "ycprop":   [142, 143, 144, 145, 146],
    "bhprop":   [152, 153, 154, 155, 156],
    "rfprop":   [162, 163, 164, 165, 166],
    "gsprop":   [172, 173, 174, 175, 176],
    "bdprop":   [182, 183, 184, 185, 186],
    "abprop":   [192, 193, 194, 195, 196],
    "jsprop":   [202, 203, 204, 205, 206],
    "ciprop":   [212, 213, 214, 215, 216],
    "pcprop":   [222, 223, 224, 225, 226],
    "tgprop":   [232, 233, 234, 235, 236],
    "plprop":   [242, 243, 244, 245, 246],
}


ANIM_ID_TO_SPEC = {
    # "seam":     [11],  # Changed to static
    "nhq":      [101, 107],
    "oshq":     [111, 117],
    "bmhq":     [121, 127],
    "gehq":     [131, 137],
    "ychq":     [141, 147],
    "bhhq":     [151, 157],
    "rfhq":     [161, 167],
    "gshq":     [171, 177],
    "bdhq":     [181, 187],
    "abhq":     [191, 197],
    "jshq":     [201, 207],
    "cihq":     [211, 217],
    "pchq":     [221, 227],
    "tghq":     [231, 237],
    "plhq":     [241, 247],
}


UNIT_ID_TO_SPEC = {
    "osunit":   list(range(101,  147)),
    "bmunit":   list(range(201,  247)),
    "geunit":   list(range(301,  347)),
    "ycunit":   list(range(401,  447)),
    "bhunit":   list(range(501,  547)),
    "rfunit":   list(range(601,  647)),
    "gsunit":   list(range(701,  747)),
    "bdunit":   list(range(801,  847)),
    "abunit":   list(range(901,  947)),
    "jsunit":   list(range(1001, 1047)),
    "ciunit":   list(range(1101, 1147)),
    "pcunit":   list(range(1201, 1247)),
    "tgunit":   list(range(1301, 1347)),
    "plunit":   list(range(1401, 1447)),
}


class AWMinimap:

    def __init__(self, awmap: AWMap) -> None:
        self.im = Image.new("RGBA", (4 * awmap.size_w, 4 * awmap.size_h))
        self.ims = []
        self.animated = False
        self.anim_buffer = []

        # Add all terrain sprites (buffer animated sprites)
        for x in range(awmap.size_w):
            for y in range(awmap.size_h):
                terr = awmap.tile(x, y).terr + (awmap.tile(x, y).t_ctry * 10)
                sprite, animated = AWMinimap.get_sprite(terr)
                if animated:
                    self.anim_buffer.append((x, y, sprite))
                    self.animated = True
                    continue
                self.im.paste(sprite, (x * 4, y * 4))

        # Add all unit sprites to buffer
        for x in range(awmap.size_w):
            for y in range(awmap.size_h):
                unit = awmap.tile(x, y).unit + (awmap.tile(x, y).u_ctry * 100)
                if unit:
                    sprite, _ = AWMinimap.get_sprite(unit, True)
                    self.animated = True
                    self.anim_buffer.append((x, y, sprite))

        # Copy map to 8 frames, then add the animated sprites
        if self.animated:
            self.ims = []
            for _ in range(8):
                self.ims.append(self.im.copy())
            for x, y, sprite in self.anim_buffer:
                for i in range(8):
                    self.ims[i].paste(
                        sprite[i],
                        (x * 4, y * 4, (x * 4) + 4, (y * 4) + 4),
                        sprite[i]
                    )

        # Smaller maps can be sized up
        if awmap.size_w * awmap.size_h <= 1600:
            if self.animated:
                for i, f in enumerate(self.ims):
                    self.ims[i] = f.resize(
                        (awmap.size_w * 8, awmap.size_h * 8)
                    )
            else:
                self.im = self.im.resize((awmap.size_w * 8, awmap.size_h * 8))

        if self.animated:
            self.im = AWMinimap.compile_gif(self.ims)

    @staticmethod
    def get_sprite(
            sprite_id: int,
            unit: bool=False
    ) -> Union[Tuple[Image.Image, bool], Tuple[List[Image.Image], bool]]:
        if unit:
            if sprite_id in [i for v in UNIT_ID_TO_SPEC.values() for i in v]:
                sprite_name = [k for k, v in UNIT_ID_TO_SPEC.items() if sprite_id in v][0]
                return AWMinimap.get_unit_sprite(sprite_name)
            else:
                return Image.new("RGBA", (4, 4)), False
        else:
            if sprite_id in [i for v in STATIC_ID_TO_SPEC.values() for i in v]:
                sprite_name = [
                    k
                    for k, v
                    in STATIC_ID_TO_SPEC.items()
                    if sprite_id in v
                ][0]
                return AWMinimap.get_static_sprite(sprite_name)
            elif sprite_id in [i for v in ANIM_ID_TO_SPEC.values() for i in v]:
                sprite_name = [k for k, v in ANIM_ID_TO_SPEC.items() if sprite_id in v][0]
                return AWMinimap.get_anim_sprite(sprite_name)
            else:
                return Image.new("RGBA", (4, 4)), False

    @staticmethod
    def get_static_sprite(sprite_name: str) -> Tuple[List[Image.Image], bool]:
        im = Image.new("RGBA", (4, 4))
        draw = ImageDraw.Draw(im)
        spec = SPEC[sprite_name]
        for _layer in spec:
            draw.point(**_layer)
        return im, False  # .resize((8, 8))

    @staticmethod
    def get_anim_sprite(sprite_name: str) -> Tuple[List[Image.Image], bool]:
        ims = []
        for _ in range(8):
            ims.append(Image.new("RGBA", (4, 4)))
        spec = SPEC[sprite_name]
        for frame in range(8):
            draw = ImageDraw.Draw(ims[frame])
            for _layer in spec:
                draw.point(xy=_layer["xy"][frame], fill=_layer["fill"][frame])
        return ims, True

    @staticmethod
    def get_unit_sprite(sprite_name: str) -> Tuple[List[Image.Image], bool]:
        ims = []
        for _ in range(8):
            ims.append(Image.new("RGBA", (4, 4)))
        spec = SPEC[sprite_name]
        for i in range(8):
            if 1 < i < 6:
                draw = ImageDraw.Draw(ims[i])
                for _layer in spec:
                    draw.point(**_layer)
        return ims, True

    # @staticmethod  # Current working
    # def compile_gif(frames: List[Image.Image]) -> Image.Image:
    #     img_bytes = BytesIO()
    #     first_frame = frames.pop(0)
    #     first_frame.save(
    #         img_bytes, "GIF", save_all=True, append_images=frames, loop=0,
    #         duration=150, optimize=False, version='GIF89a'
    #     )
    #     img_bytes.seek(0)
    #     compiled_gif = Image.open(img_bytes)
    #     return compiled_gif

    @staticmethod
    def compile_gif(frames: List[Image.Image]) -> Image.Image:

        # List for frames converted to "P" and frame palettes
        cvt_frames, frame_palettes = [], []

        # Convert frames to "P" and create frame palettes
        for i, frame in enumerate(frames):

            # Convert frame and add to converted frames list
            cvt_frame = frame.convert("P", palette=Image.ADAPTIVE)
            cvt_frames.append(cvt_frame)

            # Create palette from frame and add to frame palettes list
            pal = cvt_frame.resize((256, 1))
            pal.putdata(range(256))
            frame_palettes.append(pal.convert("RGB").getdata())

        __import__("time").sleep(1)
        for frame in cvt_frames:
            frame.show()
            pprint(frame.palette.getdata())

        # Create bytes object and save all frames to it as GIF data
        img_bytes = BytesIO()
        first_frame = cvt_frames.pop(0)
        first_frame.save(
            img_bytes, "GIF", save_all=True, append_images=cvt_frames, loop=0,
            duration=150, optimize=False, version='GIF89a'
        )
        img_bytes.seek(0)

        # Open GIF and apply palette to each frame
        compiled_gif = Image.open(img_bytes)
        iterator = ImageSequence.Iterator(compiled_gif)
        for i, frame in enumerate(iterator):
            frame.putpalette(frame_palettes[i])

        return compiled_gif

    # @staticmethod
    # def compile_gif(frames: List[Image.Image]):
    #     bin_frames = []
    #     for frame in frames:
    #         bytes_frame = BytesIO()
    #         frame.save(bytes_frame, "PNG")
    #         bytes_frame.seek(0)
    #         bin_frames.append(bytes_frame)
    #
    #     imageio_frames = []
    #     for frame in bin_frames:
    #         imageio_frame = imageio.get_reader(frame.read(), format='png')
    #         imageio_frames.append(imageio_frame)
    #
    #     imageio_gif = BytesIO()
    #     writer = imageio.get_writer(imageio_gif, format="gif", duration=150 / 1000)
    #     for frame in imageio_frames:
    #         writer.append_data(frame)
    #     # imageio_gif.name = "temp.gif"
    #     # imageio_gif.ext = "gif"
    #     imageio_gif.seek(0)
    #
    #     # imageio.mimsave("temp.gif", imageio_frames, format="gif", duration=150 / 1000)
    #     #
    #     # compiled_gif = Image.open("temp.gif")
    #     # __import__("os").remove("temp.gif")
    #     return imageio_gif

    # @staticmethod
    # def compile_gif(frames):
    #     first_frame = frames.pop(0)
    #     first_frame.save("temp.gif", "GIF", save_all=True, append_images=frames, loop=0, duration=150,
    #                      palette=Image.LANCZOS, transparency=255)
    #     compiled_gif = Image.open("temp.gif")
    #     return compiled_gif

    @property
    def map(self) -> Image.Image:
        return self.im
