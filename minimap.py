from PIL import Image, ImageDraw, ImageSequence, ImageFilter
from io import BytesIO


class Iterator(ImageSequence.Iterator):

    def __len__(self):
        _len = 0
        try:
            self.im.seek(0)
            while True:
                _ = self.__getitem__(_len)
                _len += 1
        except IndexError:
            return _len

    def len(self):
        return self.__len__()

    @property
    def animated(self):
        return len(self) > 1

    @property
    def static(self):
        return not self.animated


def layer(bitmask):
    if isinstance(bitmask, str):
        if bitmask[-2] == "b":
            bitmask = bitmask[::-1]
        bitmask = int(bitmask, 2)
    key = [(x, y) for y in range(4) for x in range(4)]
    return [key[i] for i in range(16) if 2 ** i & bitmask]


PALETTE = {
    "white":    (255, 255, 255),

    "green1":   (168, 240, 80),     # Plain light; Wood light
    "green2":   (104, 232, 56),     # Plain dark
    "green3":   (88,  200, 16),     # Wood dark; GE

    "blue1":    (112, 176, 248),    # Shoal; Reef light
    "blue2":    (56,  120, 248),    # Reef medium; River light
    "blue3":    (88,  104, 248),    # River dark; BM; Sea
    "blue4":    (54,  86,  209),    # CI light
    "blue5":    (20,  43,  135),    # CI dark

    "teal1":    (68,  172, 163),    # TG light
    "teal2":    (10,  89,  82),     # TG dark

    "grey1":    (166, 182, 153),    # JS
    "grey2":    (184, 176, 168),    # Road; Bridge; Silo
    "grey3":    (129, 127, 128),    # GS light
    "grey4":    (86,  92,  114),    # GS dark
    "grey5":    (144, 136, 120),    # Blink frame 2
    "grey6":    (208, 208, 216),    # Blink frame 3

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
    "brown2":   (104, 80,  56),     # Borders; Blink frame 1
    "brown3":   (80,  56,  24),     # Blink frame 5
    "brown4":   (128, 104, 88),     # Blink frame 6

    "black":    (0,   0,   0),      # Teleport

    "BLINK":    [(1,   1,   1),   (64,  64,  64),  (127, 127, 127), (190, 190, 190),
                 (253, 253, 253), (190, 190, 190), (127, 127, 127), (64,  64,  64)]
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
    "wood":     [
        {
            "xy":   layer("1001000000001001b0"),
            "fill": PALETTE["green1"]
        },
        {
            "xy":   layer("0110111011000000b0"),
            "fill": PALETTE["green2"]
        },
        {
            "xy":   layer("0000000100110110b0"),
            "fill": PALETTE["green3"]
        }
    ],
    "river":    [
        {
            "xy":   layer("1111001111111000b0"),
            "fill": PALETTE["blue2"]
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
    "seam":     [
        {
            "xy":   [layer("1010010110100101b0")] * 8,
            "fill": [PALETTE["brown1"]] * 8
        },
        {
            "xy":   [layer("0101101001011010b0")] * 8,
            "fill": PALETTE["BLINK"]
        }
    ],  # TODO: Change seams to static
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
}


class AWMinimap:

    def __init__(self, awmap):
        self.im = Image.new("RGBA", (4 * awmap.size_w, 4 * awmap.size_h))
        self.ims = []
        self.animated = False
        self.anim_buffer = []
        for x in range(awmap.size_w):
            for y in range(awmap.size_h):
                print(x, y)
                terr, animated = AWMinimap.get_sprite(awmap.tile(x, y).terr)
                if animated:
                    self.anim_buffer.append((x, y, terr))
                    self.animated = True
                    continue
                self.im.paste(terr, (x * 4, y * 4))
        if self.anim_buffer:
            self.ims = []
            for _ in range(8):
                self.ims.append(self.im.copy())
            for x, y, sprite in self.anim_buffer:
                for i in range(8):
                    self.ims[i].paste(sprite[i], (x * 4, y * 4))

        if awmap.size_w * awmap.size_h <= 400:
            if self.animated:
                for i in range(len(self.ims)):
                    self.ims[i] = self.ims[i].resize((awmap.size_w * 8, awmap.size_h * 8))
            else:
                self.im = self.im.resize((awmap.size_w * 8, awmap.size_h * 8))

        if self.animated:
            self.im = AWMinimap.compile_gif(self.ims)

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
        "silo":     [13, 14],
        "tele":     [],  # TODO
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
        "seam":     [11],
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
        "os":       [],
        "bm":       [],
        "ge":       [],
        "yc":       [],
        "bh":       [],
        "rf":       [],
        "gs":       [],
        "bd":       [],
        "ab":       [],
        "pc":       [],
        "tg":       [],
        "pl":       [],
    }

    @staticmethod
    def get_sprite(sprite_id):
        if sprite_id in [i for v in AWMinimap.STATIC_ID_TO_SPEC.values() for i in v]:
            sprite_name = [k for k, v in AWMinimap.STATIC_ID_TO_SPEC.items() if sprite_id in v][0]
            return AWMinimap.get_static_sprite(sprite_name)
        elif sprite_id in [i for v in AWMinimap.ANIM_ID_TO_SPEC.values() for i in v]:
            sprite_name = [k for k, v in AWMinimap.ANIM_ID_TO_SPEC.items() if sprite_id in v][0]
            return AWMinimap.get_anim_sprite(sprite_name)
        else:
            print("No Sprite")
            return Image.new("RGBA", (4, 4))

    @staticmethod
    def get_static_sprite(sprite_name):
        im = Image.new("RGBA", (4, 4))
        draw = ImageDraw.Draw(im)
        spec = SPEC[sprite_name]
        for _layer in spec:
            draw.point(**_layer)
        return im, False  # .resize((8, 8))

    @staticmethod
    def get_anim_sprite(sprite_name):
        ims = []
        for _ in range(8):
            ims.append(Image.new("RGBA", (4, 4)))
        spec = SPEC[sprite_name]
        for frame in range(8):
            draw = ImageDraw.Draw(ims[frame])
            for _layer in spec:
                draw.point(xy=_layer["xy"][frame], fill=_layer["fill"][frame])
        return ims, True  # .resize((8, 8))

    @staticmethod
    def compile_gif(frames):
        byteImgIO = BytesIO()
        first_frame = frames.pop(0)
        first_frame.save(byteImgIO, "GIF", save_all=True, append_images=frames, loop=0, duration=150, transparency=255)
        byteImgIO.seek(0)
        compiled_gif = Image.open(byteImgIO)
        return compiled_gif

    @property
    def map(self):
        return self.im


# sprites = []
# for sprite_name in ["plain", "mountain", "wood", "road", "river", "sea"]:
#     sprite = Image.new("RGBA", (4, 4))
#     draw = ImageDraw.Draw(sprite)
#     for layer in SPEC[sprite_name]:
#         draw.point(**layer)
#     sprites.append(sprite)
# testgif = AWMinimap.compile_gif(sprites)
# ims = Iterator(testgif)
# print(len(ims))
# testgif.save("TestGif.gif", save_all=True)

# giftest, _ = AWMinimap.get_anim_sprite("oshq")
# giftest = AWMinimap.compile_gif(giftest)
# giftest.save(f"oshq.gif", save_all=True)
