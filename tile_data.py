
# TODO: Combine all properties and units in MAIN with a key for country?

# Internal IDs for tile

MAIN_TERR = {
    1:      "Plain",
    2:      "Wood",
    3:      "Mountain",
    4:      "Road",
    5:      "Bridge",
    6:      "Sea",
    7:      "Shoal",
    8:      "Reef",
    9:      "River",
    10:     "Pipe",
    11:     "Seam",
    12:     "BrokenSeam",
    13:     "Silo",
    14:     "SiloEmpty",
    15:     "Ruins",

    101:    "HQ",
    102:    "City",
    103:    "Base",
    104:    "Airport",
    105:    "Seaport",
    106:    "Tower",
    107:    "Lab",

    111:    "OSHQ",
    112:    "OSCity",
    113:    "OSBase",
    114:    "OSAirport",
    115:    "OSSeaport",
    116:    "OSTower",
    117:    "OSLab",

    121:    "BMHQ",
    122:    "BMCity",
    123:    "BMBase",
    124:    "BMAirport",
    125:    "BMSeaport",
    126:    "BMTower",
    127:    "BMLab",

    131:    "GEHQ",
    132:    "GECity",
    133:    "GEBase",
    134:    "GEAirport",
    135:    "GESeaport",
    136:    "GETower",
    137:    "GELab",

    141:    "YCHQ",
    142:    "YCCity",
    143:    "YCBase",
    144:    "YCAirport",
    145:    "YCSeaport",
    146:    "YCTower",
    147:    "YCLab",

    151:    "BHHQ",
    152:    "BHCity",
    153:    "BHBase",
    154:    "BHAirport",
    155:    "BHSeaport",
    156:    "BHTower",
    157:    "BHLab",

    500:    "Volcano",
    501:    "GiantMissile",
    502:    "Fortress",
    503:    "FlyingFortressLand",
    504:    "FlyingFortressSea",
    505:    "BlackCannonNorth",
    506:    "BlackCannonSouth",
    507:    "MiniCannonNorth",
    508:    "MiniCannonSouth",
    509:    "MiniCannonEast",
    510:    "MiniCannonWest",
    511:    "LaserCannon",
    512:    "Deathray",
    513:    "Crystal",
    514:    "BlackCrystal",

    999:    "NullTile",
    -1:     "OutOfBounds",
}

# MAIN Terrain Categories
MAIN_TERR_CAT = {
    "land":         [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15],
    "sea":          [6, 8],
    "properties":   [x for x in MAIN_TERR.keys() if 100 < x < 300],
}

MAIN_TERR_CAT["land"] += MAIN_TERR_CAT["properties"]

MAIN_CTRY = {
    0:      "Neutral",
    1:      "Orange Star",
    2:      "Blue Moon",
    3:      "Green Earth",
    4:      "Yellow Comet",
    5:      "Black Hole",
}

MAIN_UNIT = {
    0:      "Empty",

    101:    "OSInfantry",
    102:    "OSMech",
    111:    "OSAPC",
    112:    "OSRecon",
    113:    "OSTank",
    114:    "OSMDTank",
    115:    "OSNeotank",
    116:    "OSMegatank",
    117:    "OSAntiAir",
    121:    "OSArtillery",
    122:    "OSRocket",
    123:    "OSMissile",
    124:    "OSPipeRunner",
    125:    "OSOozium",
    131:    "OSTCopter",
    132:    "OSBCopter",
    133:    "OSFighter",
    134:    "OSBomber",
    135:    "OSStealth",
    136:    "OSBBomb",
    141:    "OSBBoat",
    142:    "OSLander",
    143:    "OSCruiser",
    144:    "OSSubmarine",
    145:    "OSBattleship",
    146:    "OSCarrier",

    201:    "BMInfantry",
    202:    "BMMech",
    211:    "BMAPC",
    212:    "BMRecon",
    213:    "BMTank",
    214:    "BMMDTank",
    215:    "BMNeotank",
    216:    "BMMegatank",
    217:    "BMAntiAir",
    221:    "BMArtillery",
    222:    "BMRocket",
    223:    "BMMissile",
    224:    "BMPipeRunner",
    225:    "BMOozium",
    231:    "BMTCopter",
    232:    "BMBCopter",
    233:    "BMFighter",
    234:    "BMBomber",
    235:    "BMStealth",
    236:    "BMBBomb",
    241:    "BMBBoat",
    242:    "BMLander",
    243:    "BMCruiser",
    244:    "BMSubmarine",
    245:    "BMBattleship",
    246:    "BMCarrier",

    301:    "GEInfantry",
    302:    "GEMech",
    311:    "GEAPC",
    312:    "GERecon",
    313:    "GETank",
    314:    "GEMDTank",
    315:    "GENeotank",
    316:    "GEMegatank",
    317:    "GEAntiAir",
    321:    "GEArtillery",
    322:    "GERocket",
    323:    "GEMissile",
    324:    "GEPipeRunner",
    325:    "GEOozium",
    331:    "GETCopter",
    332:    "GEBCopter",
    333:    "GEFighter",
    334:    "GEBomber",
    335:    "GEStealth",
    336:    "GEBBomb",
    341:    "GEBBoat",
    342:    "GELander",
    343:    "GECruiser",
    344:    "GESubmarine",
    345:    "GEBattleship",
    346:    "GECarrier",

    401:    "YCInfantry",
    402:    "YCMech",
    411:    "YCAPC",
    412:    "YCRecon",
    413:    "YCTank",
    414:    "YCMDTank",
    415:    "YCNeotank",
    416:    "YCMegatank",
    417:    "YCAntiAir",
    421:    "YCArtillery",
    422:    "YCRocket",
    423:    "YCMissile",
    424:    "YCPipeRunner",
    425:    "YCOozium",
    431:    "YCTCopter",
    432:    "YCBCopter",
    433:    "YCFighter",
    434:    "YCBomber",
    435:    "YCStealth",
    436:    "YCBBomb",
    441:    "YCBBoat",
    442:    "YCLander",
    443:    "YCCruiser",
    444:    "YCSubmarine",
    445:    "YCBattleship",
    446:    "YCCarrier",

    501:    "BHInfantry",
    502:    "BHMech",
    511:    "BHAPC",
    512:    "BHRecon",
    513:    "BHTank",
    514:    "BHMDTank",
    515:    "BHNeotank",
    516:    "BHMegatank",
    517:    "BHAntiAir",
    521:    "BHArtillery",
    522:    "BHRocket",
    523:    "BHMissile",
    524:    "BHPipeRunner",
    525:    "BHOozium",
    531:    "BHTCopter",
    532:    "BHBCopter",
    533:    "BHFighter",
    534:    "BHBomber",
    535:    "BHStealth",
    536:    "BHBBomb",
    541:    "BHBBoat",
    542:    "BHLander",
    543:    "BHCruiser",
    544:    "BHSubmarine",
    545:    "BHBattleship",
    546:    "BHCarrier",
}

######################################
# Advance Wars Series Map Editor IDs #
######################################

AWS_TERR = {
    0:      1,    # Plain
    1:      4,    # Road
    2:      5,    # BridgeH
    3:      9,    # River
    16:     10,   # Pipe
    30:     8,    # Reef
    32:     5,    # BridgeV
    39:     7,    # Shoal
    60:     6,    # Sea
    90:     2,    # Wood
    150:    3,    # Mountain
    167:    12,   # BrokenSeam
    226:    11,   # Seam
    300:    111,  # OSHQ
    301:    112,  # OSCity
    302:    113,  # OSBase
    303:    114,  # OSAirport
    304:    115,  # OSSeaport
    305:    116,  # OSTower
    306:    117,  # NLab
    310:    121,  # BMHQ
    311:    122,  # BMCity
    312:    123,  # BMBase
    313:    124,  # BMAirport
    314:    125,  # BMSeaport
    315:    126,  # BMTower
    316:    127,  # NLab
    320:    131,  # GEHQ
    321:    132,  # GECity
    322:    133,  # GEBase
    323:    134,  # GEAirport
    324:    135,  # GESeaport
    325:    136,  # GETower
    326:    137,  # NLab
    330:    141,  # YCHQ
    331:    142,  # YCCity
    332:    143,  # YCBase
    333:    144,  # YCAirport
    334:    145,  # YCSeaport
    335:    146,  # YCTower
    336:    147,  # NLab
    340:    151,  # BHHQ
    341:    152,  # BHCity
    342:    153,  # BHBase
    343:    154,  # BHAirport
    344:    155,  # BHSeaport
    345:    156,  # BHTower
    346:    157,  # NLab
    350:    13,   # Silo
    351:    102,  # NCity
    352:    103,  # Nbase
    353:    104,  # Nairport
    354:    105,  # NSeaport
    355:    106,  # NTower
    356:    107,  # NLab
    900:    507,  # MiniCannonNorth
    901:    510,  # MiniCannonWest
    902:    511,  # LaserCannon
    907:    500,  # VolcanoNWNW
    908:    500,  # VolcanoNWN
    909:    500,  # VolcanoNEN
    910:    500,  # VolcanoNENE
    911:    501,  # GiantMissileNWNW
    912:    501,  # GiantMissileNWN
    913:    501,  # GiantMissileNEN
    914:    501,  # GiantMissileNENE
    920:    509,  # MiniCannonEast
    921:    508,  # MiniCannonSouth
    923:    513,  # Crystal
    927:    500,  # VolcanoNWW
    928:    500,  # VolcanoNW
    929:    500,  # VolcanoNE
    930:    500,  # VolcanoNEE
    931:    501,  # GiantMissileNWW
    932:    501,  # GiantMissileNW
    933:    501,  # GiantMissileNE
    934:    501,  # GiantMissileNEE
    940:    506,  # BlackCannonSouthNW
    941:    506,  # BlackCannonSouthN
    942:    506,  # BlackCannonSouthNE
    943:    505,  # BlackCannonNorthNW
    944:    505,  # BlackCannonNorthN
    945:    505,  # BlackCannonNorthNE
    947:    500,  # VolcanoSWW
    948:    500,  # VolcanoSW
    949:    500,  # VolcanoSE
    950:    500,  # VolcanoSEE
    951:    501,  # GiantMissileSWW
    952:    501,  # GiantMissileSW
    953:    501,  # GiantMissileSE
    954:    501,  # GiantMissileSEE
    960:    506,  # BlackCannonSouthW
    961:    506,  # BlackCannonSouthC
    962:    506,  # BlackCannonSouthE
    963:    505,  # BlackCannonNorthW
    964:    505,  # BlackCannonNorthC
    965:    505,  # BlackCannonNorthE
    967:    500,  # VolcanoSWSW
    968:    500,  # VolcanoSWS
    969:    500,  # VolcanoSES
    970:    500,  # VolcanoSESE
    971:    501,  # GiantMissileSWSW
    972:    501,  # GiantMissileSWS
    973:    501,  # GiantMissileSES
    974:    501,  # GiantMissileSESE
    980:    506,  # BlackCannonSouthSW
    981:    506,  # BlackCannonSouthS
    982:    506,  # BlackCannonSouthSE
    983:    505,  # BlackCannonNorthSW
    984:    505,  # BlackCannonNorthS
    985:    505,  # BlackCannonNorthSE
    987:    502,  # FortressNWNW
    988:    502,  # FortressNWN
    989:    502,  # FortressNEN
    990:    502,  # FortressNENE
    991:    503,  # FlyingFortressLandNWNW
    992:    503,  # FlyingFortressLandNWN
    993:    503,  # FlyingFortressLandNEN
    994:    503,  # FlyingFortressLandNENE
    1000:   512,  # DeathrayNW
    1001:   512,  # DeathrayN
    1002:   512,  # DeathrayNE
    1003:   514,  # BlackCrystalNW
    1004:   514,  # BlackCrystalN
    1005:   514,  # BlackCrystalNE
    1007:   502,  # FortressNWW
    1008:   502,  # FortressNW
    1009:   502,  # FortressNE
    1010:   502,  # FortressNEE
    1011:   503,  # FlyingFortressLandNWW
    1012:   503,  # FlyingFortressLandNW
    1013:   503,  # FlyingFortressLandNE
    1014:   503,  # FlyingFortressLandNEE
    1020:   512,  # DeathrayW
    1021:   512,  # DeathrayC
    1022:   512,  # DeathrayE
    1023:   514,  # BlackCrystalW
    1024:   514,  # BlackCrystalC
    1025:   514,  # BlackCrystalE
    1027:   502,  # FortressSWW
    1028:   502,  # FortressSW
    1029:   502,  # FortressSE
    1030:   502,  # FortressSEE
    1031:   503,  # FlyingFortressLandSWW
    1032:   503,  # FlyingFortressLandSW
    1033:   503,  # FlyingFortressLandSE
    1034:   503,  # FlyingFortressLandSEE
    1040:   512,  # DeathraySW
    1041:   512,  # DeathrayS
    1042:   512,  # DeathraySE
    1043:   514,  # BlackCrystalSW
    1044:   514,  # BlackCrystalS
    1045:   514,  # BlackCrystalSE
    1047:   502,  # FortressSWSW
    1048:   502,  # FortressSWS
    1049:   502,  # FortressSES
    1050:   502,  # FortressSESE
    1051:   503,  # FlyingFortressLandSWSW
    1052:   503,  # FlyingFortressLandSWS
    1053:   503,  # FlyingFortressLandSES
    1054:   503,  # FlyingFortressLandSESE  # TODO: Add Flying Fortress SEA
}

AWS_UNIT = {
    65535:  0     # Empty
}

# Relate MAIN TERR IDs to AWS TERR IDs
MAIN_TERR_TO_AWS = {k: [x for x in AWS_TERR.keys() if AWS_TERR.get(x, None) == k]
                    for k in MAIN_TERR.keys()}
MAIN_TERR_TO_AWS[14] = [350]
MAIN_TERR_TO_AWS[15] = [167]
MAIN_TERR_TO_AWS[101] = [102]

# Relate MAIN UNIT IDs to AWS UNIT IDs
MAIN_UNIT_TO_AWS = {k: [x for x in AWS_UNIT.keys() if AWS_UNIT.get(x, None) == k]
                    for k in MAIN_UNIT.keys()}
for k, v in MAIN_UNIT_TO_AWS.items():  # Non-AWBW tiles become warp-tiles
    if len(v) == 0:
        MAIN_UNIT_TO_AWS[k] = [65535]

###########################
# Advance Wars By Web IDs #
###########################

AWBW_TERR = {
    1:      1,    # Plain
    2:      3,    # Mountain
    3:      2,    # Wood
    4:      9,    # HRiver
    5:      9,    # VRiver
    6:      9,    # CRiver
    7:      9,    # ESRiver
    8:      9,    # SWRiver
    9:      9,    # WNRiver
    10:     9,    # NERiver
    11:     9,    # ESWRiver
    12:     9,    # SWNRiver
    13:     9,    # WNERiver
    14:     9,    # NESRiver
    15:     4,    # HRoad
    16:     4,    # VRoad
    17:     4,    # CRoad
    18:     4,    # ESRoad
    19:     4,    # SWRoad
    20:     4,    # WNRoad
    21:     4,    # NERoad
    22:     4,    # ESWRoad
    23:     4,    # SWNRoad
    24:     4,    # WNERoad
    25:     4,    # NESRoad
    26:     5,    # HBridge
    27:     5,    # VBridge
    28:     6,    # Sea
    29:     7,    # HShoal
    30:     7,    # HShoalN
    31:     7,    # VShoal
    32:     7,    # VShoalE
    33:     8,    # Reef
    34:     102,  # Neutral City
    35:     103,  # Neutral Base
    36:     104,  # Neutral Airport
    37:     105,  # Neutral Port
    38:     112,  # Orange Star City
    39:     113,  # Orange Star Base
    40:     114,  # Orange Star Airport
    41:     115,  # Orange Star Port
    42:     111,  # Orange Star HQ
    43:     122,  # Blue Moon City
    44:     123,  # Blue Moon Base
    45:     124,  # Blue Moon Airport
    46:     125,  # Blue Moon Port
    47:     121,  # Blue Moon HQ
    48:     132,  # Green Earth City
    49:     133,  # Green Earth Base
    50:     134,  # Green Earth Airport
    51:     135,  # Green Earth Port
    52:     131,  # Green Earth HQ
    53:     142,  # Yellow Comet City
    54:     143,  # Yellow Comet Base
    55:     144,  # Yellow Comet Airport
    56:     145,  # Yellow Comet Port
    57:     141,  # Yellow Comet HQ
    81:     999,  # Red Fire City
    82:     999,  # Red Fire Base
    83:     999,  # Red Fire Airport
    84:     999,  # Red Fire Port
    85:     999,  # Red Fire HQ
    86:     999,  # Grey Sky City
    87:     999,  # Grey Sky Base
    88:     999,  # Grey Sky Airport
    89:     999,  # Grey Sky Port
    90:     999,  # Grey Sky HQ
    91:     152,  # Black Hole City
    92:     153,  # Black Hole Base
    93:     154,  # Black Hole Airport
    94:     155,  # Black Hole Port
    95:     151,  # Black Hole HQ
    96:     999,  # Brown Desert City
    97:     999,  # Brown Desert Base
    98:     999,  # Brown Desert Airport
    99:     999,  # Brown Desert Port
    100:    999,  # Brown Desert HQ
    101:    10,   # VPipe
    102:    10,   # HPipe
    103:    10,   # NEPipe
    104:    10,   # ESPipe
    105:    10,   # SWPipe
    106:    10,   # WNPipe
    107:    10,   # NPipe End
    108:    10,   # EPipe End
    109:    10,   # SPipe End
    110:    10,   # WPipe End
    111:    13,   # Missile Silo
    112:    14,   # Missile Silo Empty
    113:    11,   # HPipe Seam
    114:    11,   # VPipe Seam
    115:    12,   # HPipe Rubble
    116:    12,   # VPipe Rubble
    117:    999,  # Amber Blaze Airport
    118:    999,  # Amber Blaze Base
    119:    999,  # Amber Blaze City
    120:    999,  # Amber Blaze HQ
    121:    999,  # Amber Blaze Port
    122:    999,  # Jade Sun Airport
    123:    999,  # Jade Sun Base
    124:    999,  # Jade Sun City
    125:    999,  # Jade Sun HQ
    126:    999,  # Jade Sun Port
    127:    999,  # Amber Blaze Com Tower
    128:    156,  # Black Hole Com Tower
    129:    126,  # Blue Moon Com Tower
    130:    999,  # Brown Desert Com Tower
    131:    136,  # Green Earth Com Tower
    132:    999,  # Jade Sun Com Tower
    133:    106,  # Neutral Com Tower
    134:    116,  # Orange Star Com Tower
    135:    999,  # Red Fire Com Tower
    136:    146,  # Yellow Comet Com Tower
    137:    999,  # Grey Sky Com Tower
    138:    999,  # Amber Blaze Lab
    139:    157,  # Black Hole Lab
    140:    127,  # Blue Moon Lab
    141:    999,  # Brown Desert Lab
    142:    137,  # Green Earth Lab
    143:    999,  # Grey Sky Lab
    144:    999,  # Jade Sun Lab
    145:    107,  # Neutral Lab
    146:    117,  # Orange Star Lab
    147:    999,  # Red Fire Lab
    148:    147,  # Yellow Comet Lab
    149:    999,  # Cobalt Ice Airport
    150:    999,  # Cobalt Ice Base
    151:    999,  # Cobalt Ice City
    152:    999,  # Cobalt Ice Com Tower
    153:    999,  # Cobalt Ice HQ
    154:    999,  # Cobalt Ice Lab
    155:    999,  # Cobalt Ice Port
    156:    999,  # Pink Cosmos Airport
    157:    999,  # Pink Cosmos Base
    158:    999,  # Pink Cosmos City
    159:    999,  # Pink Cosmos Com Tower
    160:    999,  # Pink Cosmos HQ
    161:    999,  # Pink Cosmos Lab
    162:    999,  # Pink Cosmos Port
    163:    999,  # Teal Galaxy Airport
    164:    999,  # Teal Galaxy Base
    165:    999,  # Teal Galaxy City
    166:    999,  # Teal Galaxy Com Tower
    167:    999,  # Teal Galaxy HQ
    168:    999,  # Teal Galaxy Lab
    169:    999,  # Teal Galaxy Port
    170:    999,  # Purple Lightning Airport
    171:    999,  # Purple Lightning Base
    172:    999,  # Purple Lightning City
    173:    999,  # Purple Lightning Com Tower
    174:    999,  # Purple Lightning HQ
    175:    999,  # Purple Lightning Lab
    176:    999,  # Purple Lightning Port
}

# Relate MAIN IDs to AWBW IDs
MAIN_TERR_TO_AWBW = {k: [x for x in AWBW_TERR.keys() if AWBW_TERR.get(x, None) == k]
                     for k in MAIN_TERR.keys()}
MAIN_TERR_TO_AWBW[999] = [""]
for k, v in MAIN_TERR_TO_AWBW.items():  # Non-AWBW tiles become warp-tiles
    if len(v) == 0:
        MAIN_TERR_TO_AWBW[k] = [""]

#
MAIN_TERR_TO_AWBW_AWARENESS = {
    # Roads: Offset from 15
    # Additionally aware of Bridge and Properties
    4:      {
        0:  0,
        1:  0,
        2:  1,
        3:  4,
        4:  0,
        5:  0,
        6:  3,
        7:  7,
        8:  1,
        9:  5,
        10: 1,
        11: 8,
        12: 6,
        13: 9,
        14: 10,
        15: 2
    },

    # Bridge: Offset from 26
    # Additionally aware of Land Tiles
    5:      {
        0:  0,
        1:  0,
        2:  1,
        3:  1,
        4:  0,
        5:  0,
        6:  1,
        7:  0,
        8:  1,
        9:  1,
        10: 1,
        11: 1,
        12: 1,
        13: 0,
        14: 1,
        15: 1
    },

    # Shoal: Offset from 29
    # Additionally aware of Land Tiles
    7:      {
        0:  0,
        1:  3,
        2:  1,
        3:  1,
        4:  2,
        5:  2,
        6:  1,
        7:  1,
        8:  0,
        9:  0,
        10: 0,
        11: 3,
        12: 0,
        13: 0,
        14: 2,
        15: 0
    },

    # River: Offset from 4
    # Additionally aware of Bridge
    9:      {
        0:  0,
        1:  0,
        2:  1,
        3:  4,
        4:  0,
        5:  0,
        6:  3,
        7:  7,
        8:  1,
        9:  5,
        10: 1,
        11: 8,
        12: 6,
        13: 9,
        14: 10,
        15: 2
    },

    # Pipe: Offset from 101
    # Additionally aware of Pipe Seam and Destroyed Pipe Seam
    10:     {
        0:  0,
        1:  7,
        2:  6,
        3:  4,
        4:  9,
        5:  1,
        6:  3,
        7:  1,
        8:  8,
        9:  5,
        10: 0,
        11: 0,
        12: 2,
        13: 1,
        14: 0,
        15: 1
    },

    # Pipe Seam: Offset from 113
    # Additionally aware of Pipe and Destroyed Pipe Seam
    11:     {
        0:  0,
        1:  0,
        2:  1,
        3:  0,
        4:  0,
        5:  0,
        6:  0,
        7:  0,
        8:  1,
        9:  0,
        10: 1,
        11: 1,
        12: 0,
        13: 0,
        14: 1,
        15: 0
    },

    # Destroyed Pipe Seam: Offset from 115
    # Additionally aware of Pipe and Pipe Seam
    12:     {
        0:  0,
        1:  0,
        2:  1,
        3:  0,
        4:  0,
        5:  0,
        6:  0,
        7:  0,
        8:  1,
        9:  0,
        10: 1,
        11: 1,
        12: 0,
        13: 0,
        14: 1,
        15: 0
    },

    "aware_of": {
        4:  [4, 5, 13, 14, *MAIN_TERR_CAT["properties"]],  # Road
        5:  [7, *MAIN_TERR_CAT["land"]],  # Bridge  # TODO: Figure out why bridges are ignoring awareness
        7:  [9, *MAIN_TERR_CAT["land"]],  # Shoal
        9:  [5, 9],  # River
        10: [10, 11, 12],  # Pipe
        11: [10, 11, 12],  # Pipe Seam
        12: [10, 11, 12],  # Destroyed Pipe Seam
    }
}

# print(MAIN_UNIT_TO_AWS)
