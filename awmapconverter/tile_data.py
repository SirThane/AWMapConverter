"""IDs and other tile data necessary constructing
and manipulating `AWMap` instances"""


"""###########################################
   # Advance Wars Map Converter Internal IDs #
   ###########################################"""

# MAIN terrain IDs with internal names
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
}


# Create "Categories" for terrain type for tile awareness
MAIN_TERR_CAT = {
    "land":         [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15],
    "sea":          [6, 8],
    "properties":   [101, 102, 103, 104, 105, 106, 107],
}
MAIN_TERR_CAT["land"].append(MAIN_TERR_CAT["properties"])


# MAIN unit IDs with internal names
MAIN_UNIT = {
    0:      "Empty",

    1:      "Infantry",
    2:      "Mech",
    11:     "APC",
    12:     "Recon",
    13:     "Tank",
    14:     "MDTank",
    15:     "Neotank",
    16:     "Megatank",
    17:     "AntiAir",
    21:     "Artillery",
    22:     "Rocket",
    23:     "Missile",
    24:     "PipeRunner",
    25:     "Oozium",
    31:     "TCopter",
    32:     "BCopter",
    33:     "Fighter",
    34:     "Bomber",
    35:     "Stealth",
    36:     "BBomb",
    41:     "BBoat",
    42:     "Lander",
    43:     "Cruiser",
    44:     "Submarine",
    45:     "Battleship",
    46:     "Carrier",
}


# Country IDs in country order
MAIN_CTRY = {
    0:      "Neutral",
    1:      "Orange Star",
    2:      "Blue Moon",
    3:      "Green Earth",
    4:      "Yellow Comet",
    5:      "Black Hole",
    6:      "Red Fire",
    7:      "Grey Sky",
    8:      "Brown Desert",
    9:      "Amber Blaze",
    10:     "Jade Sun",
    11:     "Cobalt Ice",
    12:     "Pink Cosmos",
    13:     "Teal Galaxy",
    14:     "Purple Lightning",
    15:     "Acid Rain",
    16:     "White Nova"
}


"""######################################
   # Advance Wars Series Map Editor IDs #
   ######################################"""

# Relate AWS terrain IDs to MAIN terrain IDs
AWS_TERR = {
    0:      (1,   0),  # Plain
    1:      (4,   0),  # Road
    2:      (5,   0),  # BridgeH  # TODO: This is why awareness fucks up
    3:      (9,   0),  # River
    16:     (10,  0),  # Pipe
    30:     (8,   0),  # Reef
    32:     (5,   0),  # BridgeV  # TODO: Guess we need AWS awareness
    39:     (7,   0),  # Shoal
    60:     (6,   0),  # Sea
    90:     (2,   0),  # Wood
    150:    (3,   0),  # Mountain
    167:    (12,  0),  # BrokenSeam
    226:    (11,  0),  # Seam
    300:    (111, 1),  # OSHQ
    301:    (112, 1),  # OSCity
    302:    (113, 1),  # OSBase
    303:    (114, 1),  # OSAirport
    304:    (115, 1),  # OSSeaport
    305:    (116, 1),  # OSTower
    306:    (117, 1),  # OSLab
    310:    (121, 2),  # BMHQ
    311:    (122, 2),  # BMCity
    312:    (123, 2),  # BMBase
    313:    (124, 2),  # BMAirport
    314:    (125, 2),  # BMSeaport
    315:    (126, 2),  # BMTower
    316:    (127, 2),  # BMLab
    320:    (131, 3),  # GEHQ
    321:    (132, 3),  # GECity
    322:    (133, 3),  # GEBase
    323:    (134, 3),  # GEAirport
    324:    (135, 3),  # GESeaport
    325:    (136, 3),  # GETower
    326:    (137, 3),  # GELab
    330:    (141, 4),  # YCHQ
    331:    (142, 4),  # YCCity
    332:    (143, 4),  # YCBase
    333:    (144, 4),  # YCAirport
    334:    (145, 4),  # YCSeaport
    335:    (146, 4),  # YCTower
    336:    (147, 4),  # YCLab
    340:    (151, 5),  # BHHQ
    341:    (152, 5),  # BHCity
    342:    (153, 5),  # BHBase
    343:    (154, 5),  # BHAirport
    344:    (155, 5),  # BHSeaport
    345:    (156, 5),  # BHTower
    346:    (157, 5),  # BHLab
    350:    (13,  0),  # Silo
    351:    (102, 0),  # NCity
    352:    (103, 0),  # NBase
    353:    (104, 0),  # NAirport
    354:    (105, 0),  # NSeaport
    355:    (106, 0),  # NTower
    356:    (107, 0),  # NLab
    900:    (507, 0),  # MiniCannonNorth
    901:    (510, 0),  # MiniCannonWest
    902:    (511, 0),  # LaserCannon
    907:    (500, 0),  # VolcanoNWNW
    908:    (500, 0),  # VolcanoNWN
    909:    (500, 0),  # VolcanoNEN
    910:    (500, 0),  # VolcanoNENE
    911:    (501, 0),  # GiantMissileNWNW
    912:    (501, 0),  # GiantMissileNWN
    913:    (501, 0),  # GiantMissileNEN
    914:    (501, 0),  # GiantMissileNENE
    920:    (509, 0),  # MiniCannonEast
    921:    (508, 0),  # MiniCannonSouth
    923:    (513, 0),  # Crystal
    927:    (500, 0),  # VolcanoNWW
    928:    (500, 0),  # VolcanoNW
    929:    (500, 0),  # VolcanoNE
    930:    (500, 0),  # VolcanoNEE
    931:    (501, 0),  # GiantMissileNWW
    932:    (501, 0),  # GiantMissileNW
    933:    (501, 0),  # GiantMissileNE
    934:    (501, 0),  # GiantMissileNEE
    940:    (506, 0),  # BlackCannonSouthNW
    941:    (506, 0),  # BlackCannonSouthN
    942:    (506, 0),  # BlackCannonSouthNE
    943:    (505, 0),  # BlackCannonNorthNW
    944:    (505, 0),  # BlackCannonNorthN
    945:    (505, 0),  # BlackCannonNorthNE
    947:    (500, 0),  # VolcanoSWW
    948:    (500, 0),  # VolcanoSW
    949:    (500, 0),  # VolcanoSE
    950:    (500, 0),  # VolcanoSEE
    951:    (501, 0),  # GiantMissileSWW
    952:    (501, 0),  # GiantMissileSW
    953:    (501, 0),  # GiantMissileSE
    954:    (501, 0),  # GiantMissileSEE
    960:    (506, 0),  # BlackCannonSouthW
    961:    (506, 0),  # BlackCannonSouthC
    962:    (506, 0),  # BlackCannonSouthE
    963:    (505, 0),  # BlackCannonNorthW
    964:    (505, 0),  # BlackCannonNorthC
    965:    (505, 0),  # BlackCannonNorthE
    967:    (500, 0),  # VolcanoSWSW
    968:    (500, 0),  # VolcanoSWS
    969:    (500, 0),  # VolcanoSES
    970:    (500, 0),  # VolcanoSESE
    971:    (501, 0),  # GiantMissileSWSW
    972:    (501, 0),  # GiantMissileSWS
    973:    (501, 0),  # GiantMissileSES
    974:    (501, 0),  # GiantMissileSESE
    980:    (506, 0),  # BlackCannonSouthSW
    981:    (506, 0),  # BlackCannonSouthS
    982:    (506, 0),  # BlackCannonSouthSE
    983:    (505, 0),  # BlackCannonNorthSW
    984:    (505, 0),  # BlackCannonNorthS
    985:    (505, 0),  # BlackCannonNorthSE
    987:    (502, 0),  # FortressNWNW
    988:    (502, 0),  # FortressNWN
    989:    (502, 0),  # FortressNEN
    990:    (502, 0),  # FortressNENE
    991:    (503, 0),  # FlyingFortressLandNWNW
    992:    (503, 0),  # FlyingFortressLandNWN
    993:    (503, 0),  # FlyingFortressLandNEN
    994:    (503, 0),  # FlyingFortressLandNENE
    1000:   (512, 0),  # DeathrayNW
    1001:   (512, 0),  # DeathrayN
    1002:   (512, 0),  # DeathrayNE
    1003:   (514, 0),  # BlackCrystalNW
    1004:   (514, 0),  # BlackCrystalN
    1005:   (514, 0),  # BlackCrystalNE
    1007:   (502, 0),  # FortressNWW
    1008:   (502, 0),  # FortressNW
    1009:   (502, 0),  # FortressNE
    1010:   (502, 0),  # FortressNEE
    1011:   (503, 0),  # FlyingFortressLandNWW
    1012:   (503, 0),  # FlyingFortressLandNW
    1013:   (503, 0),  # FlyingFortressLandNE
    1014:   (503, 0),  # FlyingFortressLandNEE
    1020:   (512, 0),  # DeathrayW
    1021:   (512, 0),  # DeathrayC
    1022:   (512, 0),  # DeathrayE
    1023:   (514, 0),  # BlackCrystalW
    1024:   (514, 0),  # BlackCrystalC
    1025:   (514, 0),  # BlackCrystalE
    1027:   (502, 0),  # FortressSWW
    1028:   (502, 0),  # FortressSW
    1029:   (502, 0),  # FortressSE
    1030:   (502, 0),  # FortressSEE
    1031:   (503, 0),  # FlyingFortressLandSWW
    1032:   (503, 0),  # FlyingFortressLandSW
    1033:   (503, 0),  # FlyingFortressLandSE
    1034:   (503, 0),  # FlyingFortressLandSEE
    1040:   (512, 0),  # DeathraySW
    1041:   (512, 0),  # DeathrayS
    1042:   (512, 0),  # DeathraySE
    1043:   (514, 0),  # BlackCrystalSW
    1044:   (514, 0),  # BlackCrystalS
    1045:   (514, 0),  # BlackCrystalSE
    1047:   (502, 0),  # FortressSWSW
    1048:   (502, 0),  # FortressSWS
    1049:   (502, 0),  # FortressSES
    1050:   (502, 0),  # FortressSESE
    1051:   (503, 0),  # FlyingFortressLandSWSW
    1052:   (503, 0),  # FlyingFortressLandSWS
    1053:   (503, 0),  # FlyingFortressLandSES
    1054:   (503, 0),  # FlyingFortressLandSESE  # TODO: Add FlyingFortress SEA
}


# Relate AWS unit IDs to MAIN unit IDs
AWS_UNIT = {
    65535:  (0,  0),     # Empty

    500:    (1,  1),   # OSInfantry
    520:    (2,  1),   # OSMech
    522:    (11, 1),   # OSAPC
    502:    (12, 1),   # OSRecon
    521:    (13, 1),   # OSTank
    501:    (14, 1),   # OSMDTank
    509:    (15, 1),   # OSNeotank
    510:    (16, 1),   # OSMegatank
    504:    (17, 1),   # OSAntiAir
    503:    (21, 1),   # OSArtillery
    523:    (22, 1),   # OSRocket
    524:    (23, 1),   # OSMissile
    511:    (24, 1),   # OSPipeRunner
    512:    (25, 1),   # OSOozium
    526:    (31, 1),   # OSTCopter
    506:    (32, 1),   # OSBCopter
    505:    (33, 1),   # OSFighter
    525:    (34, 1),   # OSBomber
    531:    (35, 1),   # OSStealth
    532:    (36, 1),   # OSBBomb
    529:    (41, 1),   # OSBBoat
    508:    (42, 1),   # OSLander
    527:    (43, 1),   # OSCruiser
    528:    (44, 1),   # OSSubmarine
    507:    (45, 1),   # OSBattleship
    530:    (46, 1),   # OSCarrier

    540:    (1,  2),   # BMInfantry
    560:    (2,  2),   # BMMech
    562:    (11, 2),   # BMAPC
    542:    (12, 2),   # BMRecon
    561:    (13, 2),   # BMTank
    541:    (14, 2),   # BMMDTank
    549:    (15, 2),   # BMNeotank
    550:    (16, 2),   # BMMegatank
    544:    (17, 2),   # BMAntiAir
    543:    (21, 2),   # BMArtillery
    563:    (22, 2),   # BMRocket
    564:    (23, 2),   # BMMissile
    551:    (24, 2),   # BMPipeRunner
    552:    (25, 2),   # BMOozium
    566:    (31, 2),   # BMTCopter
    546:    (32, 2),   # BMBCopter
    545:    (33, 2),   # BMFighter
    565:    (34, 2),   # BMBomber
    571:    (35, 2),   # BMStealth
    572:    (36, 2),   # BMBBomb
    569:    (41, 2),   # BMBBoat
    548:    (42, 2),   # BMLander
    567:    (43, 2),   # BMCruiser
    568:    (44, 2),   # BMSubmarine
    547:    (45, 2),   # BMBattleship
    570:    (46, 2),   # BMCarrier

    580:    (1,  3),   # GEInfantry
    600:    (2,  3),   # GEMech
    602:    (11, 3),   # GEAPC
    582:    (12, 3),   # GERecon
    601:    (13, 3),   # GETank
    581:    (14, 3),   # GEMDTank
    589:    (15, 3),   # GENeotank
    590:    (16, 3),   # GEMegatank
    584:    (17, 3),   # GEAntiAir
    583:    (21, 3),   # GEArtillery
    603:    (22, 3),   # GERocket
    604:    (23, 3),   # GEMissile
    591:    (24, 3),   # GEPipeRunner
    592:    (25, 3),   # GEOozium
    606:    (31, 3),   # GETCopter
    586:    (32, 3),   # GEBCopter
    585:    (33, 3),   # GEFighter
    605:    (34, 3),   # GEBomber
    611:    (35, 3),   # GEStealth
    612:    (36, 3),   # GEBBomb
    609:    (41, 3),   # GEBBoat
    588:    (42, 3),   # GELander
    607:    (43, 3),   # GECruiser
    608:    (44, 3),   # GESubmarine
    587:    (45, 3),   # GEBattleship
    610:    (46, 3),   # GECarrier

    620:    (1,  4),   # YCInfantry
    640:    (2,  4),   # YCMech
    642:    (11, 4),   # YCAPC
    622:    (12, 4),   # YCRecon
    641:    (13, 4),   # YCTank
    621:    (14, 4),   # YCMDTank
    629:    (15, 4),   # YCNeotank
    630:    (16, 4),   # YCMegatank
    624:    (17, 4),   # YCAntiAir
    623:    (21, 4),   # YCArtillery
    643:    (22, 4),   # YCRocket
    644:    (23, 4),   # YCMissile
    631:    (24, 4),   # YCPipeRunner
    632:    (25, 4),   # YCOozium
    646:    (31, 4),   # YCTCopter
    626:    (32, 4),   # YCBCopter
    625:    (33, 4),   # YCFighter
    645:    (34, 4),   # YCBomber
    651:    (35, 4),   # YCStealth
    652:    (36, 4),   # YCBBomb
    649:    (41, 4),   # YCBBoat
    628:    (42, 4),   # YCLander
    647:    (43, 4),   # YCCruiser
    648:    (44, 4),   # YCSubmarine
    627:    (45, 4),   # YCBattleship
    650:    (46, 4),   # YCCarrier

    660:    (1,  5),   # BHInfantry
    680:    (2,  5),   # BHMech
    682:    (11, 5),   # BHAPC
    662:    (12, 5),   # BHRecon
    681:    (13, 5),   # BHTank
    661:    (14, 5),   # BHMDTank
    669:    (15, 5),   # BHNeotank
    670:    (16, 5),   # BHMegatank
    664:    (17, 5),   # BHAntiAir
    663:    (21, 5),   # BHArtillery
    683:    (22, 5),   # BHRocket
    684:    (23, 5),   # BHMissile
    671:    (24, 5),   # BHPipeRunner
    672:    (25, 5),   # BHOozium
    686:    (31, 5),   # BHTCopter
    666:    (32, 5),   # BHBCopter
    665:    (33, 5),   # BHFighter
    685:    (34, 5),   # BHBomber
    691:    (35, 5),   # BHStealth
    692:    (36, 5),   # BHBBomb
    689:    (41, 5),   # BHBBoat
    668:    (42, 5),   # BHLander
    687:    (43, 5),   # BHCruiser
    688:    (44, 5),   # BHSubmarine
    667:    (45, 5),   # BHBattleship
    690:    (46, 5),   # BHCarrier
}


def main_terr_to_aws(terr: int=1, ctry: int=0) -> list:
    default_value = [0]
    override = {
        14:  350,  # EmptySilo overridden to Silo
        15:  167,  # Ruin      overridden to BrokenSeam
        101: 102,  # NHQ       overridden to NCity
        999: 921,  # NullTile  overridden to MinicannonSouth
    }
    match = []
    for k, v in AWS_TERR.items():
        if terr in override.keys():
            match.append(override[terr])
            break
        if (terr, ctry) == v:
            match.append(k)
    if match:
        return match
    else:
        return default_value


def main_unit_to_aws(unit: int=0, ctry: int=1) -> list:
    default_value = [65535]
    match = []
    for k, v in AWS_UNIT.items():
        if (unit, ctry) == v:
            match.append(k)
    if match:
        return match
    else:
        return default_value


"""###########################
   # Advance Wars By Web IDs #
   ###########################"""

# # Relate AWBW terrain IDs to MAIN terrain IDs
# AWBW_TERR = {
#     "":     999,  # Teleport Tile
#     1:      1,    # Plain
#     2:      3,    # Mountain
#     3:      2,    # Wood
#     4:      9,    # HRiver
#     5:      9,    # VRiver
#     6:      9,    # CRiver
#     7:      9,    # ESRiver
#     8:      9,    # SWRiver
#     9:      9,    # WNRiver
#     10:     9,    # NERiver
#     11:     9,    # ESWRiver
#     12:     9,    # SWNRiver
#     13:     9,    # WNERiver
#     14:     9,    # NESRiver
#     15:     4,    # HRoad
#     16:     4,    # VRoad
#     17:     4,    # CRoad
#     18:     4,    # ESRoad
#     19:     4,    # SWRoad
#     20:     4,    # WNRoad
#     21:     4,    # NERoad
#     22:     4,    # ESWRoad
#     23:     4,    # SWNRoad
#     24:     4,    # WNERoad
#     25:     4,    # NESRoad
#     26:     5,    # HBridge
#     27:     5,    # VBridge
#     28:     6,    # Sea
#     29:     7,    # HShoal
#     30:     7,    # HShoalN
#     31:     7,    # VShoal
#     32:     7,    # VShoalE
#     33:     8,    # Reef
#     34:     102,  # Neutral City
#     35:     103,  # Neutral Base
#     36:     104,  # Neutral Airport
#     37:     105,  # Neutral Port
#     38:     112,  # Orange Star City
#     39:     113,  # Orange Star Base
#     40:     114,  # Orange Star Airport
#     41:     115,  # Orange Star Port
#     42:     111,  # Orange Star HQ
#     43:     122,  # Blue Moon City
#     44:     123,  # Blue Moon Base
#     45:     124,  # Blue Moon Airport
#     46:     125,  # Blue Moon Port
#     47:     121,  # Blue Moon HQ
#     48:     132,  # Green Earth City
#     49:     133,  # Green Earth Base
#     50:     134,  # Green Earth Airport
#     51:     135,  # Green Earth Port
#     52:     131,  # Green Earth HQ
#     53:     142,  # Yellow Comet City
#     54:     143,  # Yellow Comet Base
#     55:     144,  # Yellow Comet Airport
#     56:     145,  # Yellow Comet Port
#     57:     141,  # Yellow Comet HQ
#     81:     162,  # Red Fire City
#     82:     163,  # Red Fire Base
#     83:     164,  # Red Fire Airport
#     84:     165,  # Red Fire Port
#     85:     161,  # Red Fire HQ
#     86:     172,  # Grey Sky City
#     87:     173,  # Grey Sky Base
#     88:     174,  # Grey Sky Airport
#     89:     175,  # Grey Sky Port
#     90:     171,  # Grey Sky HQ
#     91:     152,  # Black Hole City
#     92:     153,  # Black Hole Base
#     93:     154,  # Black Hole Airport
#     94:     155,  # Black Hole Port
#     95:     151,  # Black Hole HQ
#     96:     182,  # Brown Desert City
#     97:     183,  # Brown Desert Base
#     98:     184,  # Brown Desert Airport
#     99:     185,  # Brown Desert Port
#     100:    181,  # Brown Desert HQ
#     101:    10,   # VPipe
#     102:    10,   # HPipe
#     103:    10,   # NEPipe
#     104:    10,   # ESPipe
#     105:    10,   # SWPipe
#     106:    10,   # WNPipe
#     107:    10,   # NPipe End
#     108:    10,   # EPipe End
#     109:    10,   # SPipe End
#     110:    10,   # WPipe End
#     111:    13,   # Missile Silo
#     112:    14,   # Missile Silo Empty
#     113:    11,   # HPipe Seam
#     114:    11,   # VPipe Seam
#     115:    12,   # HPipe Rubble
#     116:    12,   # VPipe Rubble
#     117:    194,  # Amber Blaze Airport
#     118:    193,  # Amber Blaze Base
#     119:    192,  # Amber Blaze City
#     120:    191,  # Amber Blaze HQ
#     121:    195,  # Amber Blaze Port
#     122:    204,  # Jade Sun Airport
#     123:    203,  # Jade Sun Base
#     124:    202,  # Jade Sun City
#     125:    201,  # Jade Sun HQ
#     126:    205,  # Jade Sun Port
#     127:    196,  # Amber Blaze Com Tower
#     128:    156,  # Black Hole Com Tower
#     129:    126,  # Blue Moon Com Tower
#     130:    186,  # Brown Desert Com Tower
#     131:    136,  # Green Earth Com Tower
#     132:    206,  # Jade Sun Com Tower
#     133:    106,  # Neutral Com Tower
#     134:    116,  # Orange Star Com Tower
#     135:    166,  # Red Fire Com Tower
#     136:    146,  # Yellow Comet Com Tower
#     137:    176,  # Grey Sky Com Tower
#     138:    197,  # Amber Blaze Lab
#     139:    157,  # Black Hole Lab
#     140:    127,  # Blue Moon Lab
#     141:    187,  # Brown Desert Lab
#     142:    137,  # Green Earth Lab
#     143:    177,  # Grey Sky Lab
#     144:    207,  # Jade Sun Lab
#     145:    107,  # Neutral Lab
#     146:    117,  # Orange Star Lab
#     147:    167,  # Red Fire Lab
#     148:    147,  # Yellow Comet Lab
#     149:    214,  # Cobalt Ice Airport
#     150:    213,  # Cobalt Ice Base
#     151:    212,  # Cobalt Ice City
#     152:    216,  # Cobalt Ice Com Tower
#     153:    211,  # Cobalt Ice HQ
#     154:    217,  # Cobalt Ice Lab
#     155:    215,  # Cobalt Ice Port
#     156:    224,  # Pink Cosmos Airport
#     157:    223,  # Pink Cosmos Base
#     158:    222,  # Pink Cosmos City
#     159:    226,  # Pink Cosmos Com Tower
#     160:    221,  # Pink Cosmos HQ
#     161:    227,  # Pink Cosmos Lab
#     162:    225,  # Pink Cosmos Port
#     163:    234,  # Teal Galaxy Airport
#     164:    233,  # Teal Galaxy Base
#     165:    232,  # Teal Galaxy City
#     166:    236,  # Teal Galaxy Com Tower
#     167:    231,  # Teal Galaxy HQ
#     168:    237,  # Teal Galaxy Lab
#     169:    235,  # Teal Galaxy Port
#     170:    244,  # Purple Lightning Airport
#     171:    243,  # Purple Lightning Base
#     172:    242,  # Purple Lightning City
#     173:    246,  # Purple Lightning Com Tower
#     174:    241,  # Purple Lightning HQ
#     175:    247,  # Purple Lightning Lab
#     176:    245,  # Purple Lightning Port
# }


# Relate AWBW terrain IDs to MAIN terrain IDs
AWBW_TERR = {
    "":     (999,  0),  # Teleport Tile
    1:      (1,    0),  # Plain
    2:      (3,    0),  # Mountain
    3:      (2,    0),  # Wood
    4:      (9,    0),  # HRiver
    5:      (9,    0),  # VRiver
    6:      (9,    0),  # CRiver
    7:      (9,    0),  # ESRiver
    8:      (9,    0),  # SWRiver
    9:      (9,    0),  # WNRiver
    10:     (9,    0),  # NERiver
    11:     (9,    0),  # ESWRiver
    12:     (9,    0),  # SWNRiver
    13:     (9,    0),  # WNERiver
    14:     (9,    0),  # NESRiver
    15:     (4,    0),  # HRoad
    16:     (4,    0),  # VRoad
    17:     (4,    0),  # CRoad
    18:     (4,    0),  # ESRoad
    19:     (4,    0),  # SWRoad
    20:     (4,    0),  # WNRoad
    21:     (4,    0),  # NERoad
    22:     (4,    0),  # ESWRoad
    23:     (4,    0),  # SWNRoad
    24:     (4,    0),  # WNERoad
    25:     (4,    0),  # NESRoad
    26:     (5,    0),  # HBridge
    27:     (5,    0),  # VBridge
    28:     (6,    0),  # Sea
    29:     (7,    0),  # HShoal
    30:     (7,    0),  # HShoalN
    31:     (7,    0),  # VShoal
    32:     (7,    0),  # VShoalE
    33:     (8,    0),  # Reef
    34:     (102,  0),  # Neutral City
    35:     (103,  0),  # Neutral Base
    36:     (104,  0),  # Neutral Airport
    37:     (105,  0),  # Neutral Port
    38:     (102,  1),  # Orange Star City
    39:     (103,  1),  # Orange Star Base
    40:     (104,  1),  # Orange Star Airport
    41:     (105,  1),  # Orange Star Port
    42:     (101,  1),  # Orange Star HQ
    43:     (102,  2),  # Blue Moon City
    44:     (103,  2),  # Blue Moon Base
    45:     (104,  2),  # Blue Moon Airport
    46:     (105,  2),  # Blue Moon Port
    47:     (101,  2),  # Blue Moon HQ
    48:     (102,  3),  # Green Earth City
    49:     (103,  3),  # Green Earth Base
    50:     (104,  3),  # Green Earth Airport
    51:     (105,  3),  # Green Earth Port
    52:     (101,  3),  # Green Earth HQ
    53:     (102,  4),  # Yellow Comet City
    54:     (103,  4),  # Yellow Comet Base
    55:     (104,  4),  # Yellow Comet Airport
    56:     (105,  4),  # Yellow Comet Port
    57:     (101,  4),  # Yellow Comet HQ
    81:     (102,  6),  # Red Fire City
    82:     (103,  6),  # Red Fire Base
    83:     (104,  6),  # Red Fire Airport
    84:     (105,  6),  # Red Fire Port
    85:     (101,  6),  # Red Fire HQ
    86:     (102,  7),  # Grey Sky City
    87:     (103,  7),  # Grey Sky Base
    88:     (104,  7),  # Grey Sky Airport
    89:     (105,  7),  # Grey Sky Port
    90:     (101,  7),  # Grey Sky HQ
    91:     (102,  5),  # Black Hole City
    92:     (103,  5),  # Black Hole Base
    93:     (104,  5),  # Black Hole Airport
    94:     (105,  5),  # Black Hole Port
    95:     (101,  5),  # Black Hole HQ
    96:     (102,  8),  # Brown Desert City
    97:     (103,  8),  # Brown Desert Base
    98:     (104,  8),  # Brown Desert Airport
    99:     (105,  8),  # Brown Desert Port
    100:    (101,  8),  # Brown Desert HQ
    101:    (10,   0),  # VPipe
    102:    (10,   0),  # HPipe
    103:    (10,   0),  # NEPipe
    104:    (10,   0),  # ESPipe
    105:    (10,   0),  # SWPipe
    106:    (10,   0),  # WNPipe
    107:    (10,   0),  # NPipe End
    108:    (10,   0),  # EPipe End
    109:    (10,   0),  # SPipe End
    110:    (10,   0),  # WPipe End
    111:    (13,   0),  # Missile Silo
    112:    (14,   0),  # Missile Silo Empty
    113:    (11,   0),  # HPipe Seam
    114:    (11,   0),  # VPipe Seam
    115:    (12,   0),  # HPipe Rubble
    116:    (12,   0),  # VPipe Rubble
    117:    (104,  9),  # Amber Blaze Airport
    118:    (103,  9),  # Amber Blaze Base
    119:    (102,  9),  # Amber Blaze City
    120:    (101,  9),  # Amber Blaze HQ
    121:    (105,  9),  # Amber Blaze Port
    122:    (104, 10),  # Jade Sun Airport
    123:    (103, 10),  # Jade Sun Base
    124:    (102, 10),  # Jade Sun City
    125:    (101, 10),  # Jade Sun HQ
    126:    (105, 10),  # Jade Sun Port
    127:    (106,  9),  # Amber Blaze Com Tower
    128:    (106,  5),  # Black Hole Com Tower
    129:    (106,  2),  # Blue Moon Com Tower
    130:    (106,  8),  # Brown Desert Com Tower
    131:    (106,  3),  # Green Earth Com Tower
    132:    (106, 10),  # Jade Sun Com Tower
    133:    (106,  0),  # Neutral Com Tower
    134:    (106,  1),  # Orange Star Com Tower
    135:    (106,  6),  # Red Fire Com Tower
    136:    (106,  4),  # Yellow Comet Com Tower
    137:    (106,  7),  # Grey Sky Com Tower
    138:    (107,  9),  # Amber Blaze Lab
    139:    (107,  5),  # Black Hole Lab
    140:    (107,  2),  # Blue Moon Lab
    141:    (107,  8),  # Brown Desert Lab
    142:    (107,  3),  # Green Earth Lab
    143:    (107,  7),  # Grey Sky Lab
    144:    (107, 10),  # Jade Sun Lab
    145:    (107,  0),  # Neutral Lab
    146:    (107,  1),  # Orange Star Lab
    147:    (107,  6),  # Red Fire Lab
    148:    (107,  4),  # Yellow Comet Lab
    149:    (104, 11),  # Cobalt Ice Airport
    150:    (103, 11),  # Cobalt Ice Base
    151:    (102, 11),  # Cobalt Ice City
    152:    (106, 11),  # Cobalt Ice Com Tower
    153:    (101, 11),  # Cobalt Ice HQ
    154:    (107, 11),  # Cobalt Ice Lab
    155:    (105, 11),  # Cobalt Ice Port
    156:    (104, 12),  # Pink Cosmos Airport
    157:    (103, 12),  # Pink Cosmos Base
    158:    (102, 12),  # Pink Cosmos City
    159:    (106, 12),  # Pink Cosmos Com Tower
    160:    (101, 12),  # Pink Cosmos HQ
    161:    (107, 12),  # Pink Cosmos Lab
    162:    (105, 12),  # Pink Cosmos Port
    163:    (104, 13),  # Teal Galaxy Airport
    164:    (103, 13),  # Teal Galaxy Base
    165:    (102, 13),  # Teal Galaxy City
    166:    (106, 13),  # Teal Galaxy Com Tower
    167:    (101, 13),  # Teal Galaxy HQ
    168:    (107, 13),  # Teal Galaxy Lab
    169:    (105, 13),  # Teal Galaxy Port
    170:    (104, 14),  # Purple Lightning Airport
    171:    (103, 14),  # Purple Lightning Base
    172:    (102, 14),  # Purple Lightning City
    173:    (106, 14),  # Purple Lightning Com Tower
    174:    (101, 14),  # Purple Lightning HQ
    175:    (107, 14),  # Purple Lightning Lab
    176:    (105, 14),  # Purple Lightning Port
    181:    (104, 15),  # Acid Rain Airport
    182:    (103, 15),  # Acid Rain Base
    183:    (102, 15),  # Acid Rain City
    184:    (106, 15),  # Acid Rain Com Tower
    185:    (101, 15),  # Acid Rain HQ
    186:    (107, 15),  # Acid Rain Lab
    187:    (105, 15),  # Acid Rain Port
    188:    (104, 16),  # White Nova Airport
    189:    (103, 16),  # White Nova Base
    190:    (102, 16),  # White Nova City
    191:    (106, 16),  # White Nova Com Tower
    192:    (101, 16),  # White Nova HQ
    193:    (107, 16),  # White Nova Lab
    194:    (105, 16),  # White Nova Port
}


def main_terr_to_awbw(terr: int = 1, ctry: int = 0) -> list:
    default_value = [""]
    match = []
    for k, v in AWBW_TERR.items():
        if (terr, ctry) == v:
            match.append(k)
    if match:
        return match
    else:
        return default_value


# Relate AWBW unit GIF name to MAIN unit IDs
AWBW_UNIT_SPRITE = {
    'osinfantry.gif':       (1,  1),
    'bminfantry.gif':       (1,  2),
    'geinfantry.gif':       (1,  3),
    'ycinfantry.gif':       (1,  4),
    'bhinfantry.gif':       (1,  5),
    'rfinfantry.gif':       (1,  6),
    'gsinfantry.gif':       (1,  7),
    'bdinfantry.gif':       (1,  8),
    'abinfantry.gif':       (1,  9),
    'jsinfantry.gif':       (1, 10),
    'ciinfantry.gif':       (1, 11),
    'pcinfantry.gif':       (1, 12),
    'tginfantry.gif':       (1, 13),
    'plinfantry.gif':       (1, 14),

    'osmech.gif':           (2,  1),
    'bmmech.gif':           (2,  2),
    'gemech.gif':           (2,  3),
    'ycmech.gif':           (2,  4),
    'bhmech.gif':           (2,  5),
    'rfmech.gif':           (2,  6),
    'gsmech.gif':           (2,  7),
    'bdmech.gif':           (2,  8),
    'abmech.gif':           (2,  9),
    'jsmech.gif':           (2, 10),
    'cimech.gif':           (2, 11),
    'pcmech.gif':           (2, 12),
    'tgmech.gif':           (2, 13),
    'plmech.gif':           (2, 14),

    'osapc.gif':            (11,  1),
    'bmapc.gif':            (11,  2),
    'geapc.gif':            (11,  3),
    'ycapc.gif':            (11,  4),
    'bhapc.gif':            (11,  5),
    'rfapc.gif':            (11,  6),
    'gsapc.gif':            (11,  7),
    'bdapc.gif':            (11,  8),
    'abapc.gif':            (11,  9),
    'jsapc.gif':            (11, 10),
    'ciapc.gif':            (11, 11),
    'pcapc.gif':            (11, 12),
    'tgapc.gif':            (11, 13),
    'plapc.gif':            (11, 14),

    'osrecon.gif':          (12,  1),
    'bmrecon.gif':          (12,  2),
    'gerecon.gif':          (12,  3),
    'ycrecon.gif':          (12,  4),
    'bhrecon.gif':          (12,  5),
    'rfrecon.gif':          (12,  6),
    'gsrecon.gif':          (12,  7),
    'bdrecon.gif':          (12,  8),
    'abrecon.gif':          (12,  9),
    'jsrecon.gif':          (12, 10),
    'cirecon.gif':          (12, 11),
    'pcrecon.gif':          (12, 12),
    'tgrecon.gif':          (12, 13),
    'plrecon.gif':          (12, 14),

    'ostank.gif':           (13,  1),
    'bmtank.gif':           (13,  2),
    'getank.gif':           (13,  3),
    'yctank.gif':           (13,  4),
    'bhtank.gif':           (13,  5),
    'rftank.gif':           (13,  6),
    'gstank.gif':           (13,  7),
    'bdtank.gif':           (13,  8),
    'abtank.gif':           (13,  9),
    'jstank.gif':           (13, 10),
    'citank.gif':           (13, 11),
    'pctank.gif':           (13, 12),
    'tgtank.gif':           (13, 13),
    'pltank.gif':           (13, 14),

    'osmd.tank.gif':        (14,  1),
    'bmmd.tank.gif':        (14,  2),
    'gemd.tank.gif':        (14,  3),
    'ycmd.tank.gif':        (14,  4),
    'bhmd.tank.gif':        (14,  5),
    'rfmd.tank.gif':        (14,  6),
    'gsmd.tank.gif':        (14,  7),
    'bdmd.tank.gif':        (14,  8),
    'abmd.tank.gif':        (14,  9),
    'jsmd.tank.gif':        (14, 10),
    'cimd.tank.gif':        (14, 11),
    'pcmd.tank.gif':        (14, 12),
    'tgmd.tank.gif':        (14, 13),
    'plmd.tank.gif':        (14, 14),

    'osneotank.gif':        (15,  1),
    'bmneotank.gif':        (15,  2),
    'geneotank.gif':        (15,  3),
    'ycneotank.gif':        (15,  4),
    'bhneotank.gif':        (15,  5),
    'rfneotank.gif':        (15,  6),
    'gsneotank.gif':        (15,  7),
    'bdneotank.gif':        (15,  8),
    'abneotank.gif':        (15,  9),
    'jsneotank.gif':        (15, 10),
    'cineotank.gif':        (15, 11),
    'pcneotank.gif':        (15, 12),
    'tgneotank.gif':        (15, 13),
    'plneotank.gif':        (15, 14),

    'osmegatank.gif':       (16,  1),
    'bmmegatank.gif':       (16,  2),
    'gemegatank.gif':       (16,  3),
    'ycmegatank.gif':       (16,  4),
    'bhmegatank.gif':       (16,  5),
    'rfmegatank.gif':       (16,  6),
    'gsmegatank.gif':       (16,  7),
    'bdmegatank.gif':       (16,  8),
    'abmegatank.gif':       (16,  9),
    'jsmegatank.gif':       (16, 10),
    'cimegatank.gif':       (16, 11),
    'pcmegatank.gif':       (16, 12),
    'tgmegatank.gif':       (16, 13),
    'plmegatank.gif':       (16, 14),

    'osanti-air.gif':       (17,  1),
    'bmanti-air.gif':       (17,  2),
    'geanti-air.gif':       (17,  3),
    'ycanti-air.gif':       (17,  4),
    'bhanti-air.gif':       (17,  5),
    'rfanti-air.gif':       (17,  6),
    'gsanti-air.gif':       (17,  7),
    'bdanti-air.gif':       (17,  8),
    'abanti-air.gif':       (17,  9),
    'jsanti-air.gif':       (17, 10),
    'cianti-air.gif':       (17, 11),
    'pcanti-air.gif':       (17, 12),
    'tganti-air.gif':       (17, 13),
    'planti-air.gif':       (17, 14),

    'osartillery.gif':      (21,  1),
    'bmartillery.gif':      (21,  2),
    'geartillery.gif':      (21,  3),
    'ycartillery.gif':      (21,  4),
    'bhartillery.gif':      (21,  5),
    'rfartillery.gif':      (21,  6),
    'gsartillery.gif':      (21,  7),
    'bdartillery.gif':      (21,  8),
    'abartillery.gif':      (21,  9),
    'jsartillery.gif':      (21, 10),
    'ciartillery.gif':      (21, 11),
    'pcartillery.gif':      (21, 12),
    'tgartillery.gif':      (21, 13),
    'plartillery.gif':      (21, 14),

    'osrocket.gif':         (22,  1),
    'bmrocket.gif':         (22,  2),
    'gerocket.gif':         (22,  3),
    'ycrocket.gif':         (22,  4),
    'bhrocket.gif':         (22,  5),
    'rfrocket.gif':         (22,  6),
    'gsrocket.gif':         (22,  7),
    'bdrocket.gif':         (22,  8),
    'abrocket.gif':         (22,  9),
    'jsrocket.gif':         (22, 10),
    'cirocket.gif':         (22, 11),
    'pcrocket.gif':         (22, 12),
    'tgrocket.gif':         (22, 13),
    'plrocket.gif':         (22, 14),

    'osmissile.gif':        (23,  1),
    'bmmissile.gif':        (23,  2),
    'gemissile.gif':        (23,  3),
    'ycmissile.gif':        (23,  4),
    'bhmissile.gif':        (23,  5),
    'rfmissile.gif':        (23,  6),
    'gsmissile.gif':        (23,  7),
    'bdmissile.gif':        (23,  8),
    'abmissile.gif':        (23,  9),
    'jsmissile.gif':        (23, 10),
    'cimissile.gif':        (23, 11),
    'pcmissile.gif':        (23, 12),
    'tgmissile.gif':        (23, 13),
    'plmissile.gif':        (23, 14),

    'ospiperunner.gif':     (24,  1),
    'bmpiperunner.gif':     (24,  2),
    'gepiperunner.gif':     (24,  3),
    'ycpiperunner.gif':     (24,  4),
    'bhpiperunner.gif':     (24,  5),
    'rfpiperunner.gif':     (24,  6),
    'gspiperunner.gif':     (24,  7),
    'bdpiperunner.gif':     (24,  8),
    'abpiperunner.gif':     (24,  9),
    'jspiperunner.gif':     (24, 10),
    'cipiperunner.gif':     (24, 11),
    'pcpiperunner.gif':     (24, 12),
    'tgpiperunner.gif':     (24, 13),
    'plpiperunner.gif':     (24, 14),

    'ost-copter.gif':       (31,  1),
    'bmt-copter.gif':       (31,  2),
    'get-copter.gif':       (31,  3),
    'yct-copter.gif':       (31,  4),
    'bht-copter.gif':       (31,  5),
    'rft-copter.gif':       (31,  6),
    'gst-copter.gif':       (31,  7),
    'bdt-copter.gif':       (31,  8),
    'abt-copter.gif':       (31,  9),
    'jst-copter.gif':       (31, 10),
    'cit-copter.gif':       (31, 11),
    'pct-copter.gif':       (31, 12),
    'tgt-copter.gif':       (31, 13),
    'plt-copter.gif':       (31, 14),

    'osb-copter.gif':       (32,  1),
    'bmb-copter.gif':       (32,  2),
    'geb-copter.gif':       (32,  3),
    'ycb-copter.gif':       (32,  4),
    'bhb-copter.gif':       (32,  5),
    'rfb-copter.gif':       (32,  6),
    'gsb-copter.gif':       (32,  7),
    'bdb-copter.gif':       (32,  8),
    'abb-copter.gif':       (32,  9),
    'jsb-copter.gif':       (32, 10),
    'cib-copter.gif':       (32, 11),
    'pcb-copter.gif':       (32, 12),
    'tgb-copter.gif':       (32, 13),
    'plb-copter.gif':       (32, 14),

    'osfighter.gif':        (33,  1),
    'bmfighter.gif':        (33,  2),
    'gefighter.gif':        (33,  3),
    'ycfighter.gif':        (33,  4),
    'bhfighter.gif':        (33,  5),
    'rffighter.gif':        (33,  6),
    'gsfighter.gif':        (33,  7),
    'bdfighter.gif':        (33,  8),
    'abfighter.gif':        (33,  9),
    'jsfighter.gif':        (33, 10),
    'cifighter.gif':        (33, 11),
    'pcfighter.gif':        (33, 12),
    'tgfighter.gif':        (33, 13),
    'plfighter.gif':        (33, 14),

    'osbomber.gif':         (34,  1),
    'bmbomber.gif':         (34,  2),
    'gebomber.gif':         (34,  3),
    'ycbomber.gif':         (34,  4),
    'bhbomber.gif':         (34,  5),
    'rfbomber.gif':         (34,  6),
    'gsbomber.gif':         (34,  7),
    'bdbomber.gif':         (34,  8),
    'abbomber.gif':         (34,  9),
    'jsbomber.gif':         (34, 10),
    'cibomber.gif':         (34, 11),
    'pcbomber.gif':         (34, 12),
    'tgbomber.gif':         (34, 13),
    'plbomber.gif':         (34, 14),

    'osstealth.gif':        (35,  1),
    'bmstealth.gif':        (35,  2),
    'gestealth.gif':        (35,  3),
    'ycstealth.gif':        (35,  4),
    'bhstealth.gif':        (35,  5),
    'rfstealth.gif':        (35,  6),
    'gsstealth.gif':        (35,  7),
    'bdstealth.gif':        (35,  8),
    'abstealth.gif':        (35,  9),
    'jsstealth.gif':        (35, 10),
    'cistealth.gif':        (35, 11),
    'pcstealth.gif':        (35, 12),
    'tgstealth.gif':        (35, 13),
    'plstealth.gif':        (35, 14),

    'osblackbomb.gif':      (36,  1),
    'bmblackbomb.gif':      (36,  2),
    'geblackbomb.gif':      (36,  3),
    'ycblackbomb.gif':      (36,  4),
    'bhblackbomb.gif':      (36,  5),
    'rfblackbomb.gif':      (36,  6),
    'gsblackbomb.gif':      (36,  7),
    'bdblackbomb.gif':      (36,  8),
    'abblackbomb.gif':      (36,  9),
    'jsblackbomb.gif':      (36, 10),
    'ciblackbomb.gif':      (36, 11),
    'pcblackbomb.gif':      (36, 12),
    'tgblackbomb.gif':      (36, 13),
    'plblackbomb.gif':      (36, 14),

    'osblackboat.gif':      (41,  1),
    'bmblackboat.gif':      (41,  2),
    'geblackboat.gif':      (41,  3),
    'ycblackboat.gif':      (41,  4),
    'bhblackboat.gif':      (41,  5),
    'rfblackboat.gif':      (41,  6),
    'gsblackboat.gif':      (41,  7),
    'bdblackboat.gif':      (41,  8),
    'abblackboat.gif':      (41,  9),
    'jsblackboat.gif':      (41, 10),
    'ciblackboat.gif':      (41, 11),
    'pcblackboat.gif':      (41, 12),
    'tgblackboat.gif':      (41, 13),
    'plblackboat.gif':      (41, 14),

    'oslander.gif':         (42,  1),
    'bmlander.gif':         (42,  2),
    'gelander.gif':         (42,  3),
    'yclander.gif':         (42,  4),
    'bhlander.gif':         (42,  5),
    'rflander.gif':         (42,  6),
    'gslander.gif':         (42,  7),
    'bdlander.gif':         (42,  8),
    'ablander.gif':         (42,  9),
    'jslander.gif':         (42, 10),
    'cilander.gif':         (42, 11),
    'pclander.gif':         (42, 12),
    'tglander.gif':         (42, 13),
    'pllander.gif':         (42, 14),

    'oscruiser.gif':        (43,  1),
    'bmcruiser.gif':        (43,  2),
    'gecruiser.gif':        (43,  3),
    'yccruiser.gif':        (43,  4),
    'bhcruiser.gif':        (43,  5),
    'rfcruiser.gif':        (43,  6),
    'gscruiser.gif':        (43,  7),
    'bdcruiser.gif':        (43,  8),
    'abcruiser.gif':        (43,  9),
    'jscruiser.gif':        (43, 10),
    'cicruiser.gif':        (43, 11),
    'pccruiser.gif':        (43, 12),
    'tgcruiser.gif':        (43, 13),
    'plcruiser.gif':        (43, 14),

    'ossub.gif':            (44,  1),
    'bmsub.gif':            (44,  2),
    'gesub.gif':            (44,  3),
    'ycsub.gif':            (44,  4),
    'bhsub.gif':            (44,  5),
    'rfsub.gif':            (44,  6),
    'gssub.gif':            (44,  7),
    'bdsub.gif':            (44,  8),
    'absub.gif':            (44,  9),
    'jssub.gif':            (44, 10),
    'cisub.gif':            (44, 11),
    'pcsub.gif':            (44, 12),
    'tgsub.gif':            (44, 13),
    'plsub.gif':            (44, 14),

    'osbattleship.gif':     (45,  1),
    'bmbattleship.gif':     (45,  2),
    'gebattleship.gif':     (45,  3),
    'ycbattleship.gif':     (45,  4),
    'bhbattleship.gif':     (45,  5),
    'rfbattleship.gif':     (45,  6),
    'gsbattleship.gif':     (45,  7),
    'bdbattleship.gif':     (45,  8),
    'abbattleship.gif':     (45,  9),
    'jsbattleship.gif':     (45, 10),
    'cibattleship.gif':     (45, 11),
    'pcbattleship.gif':     (45, 12),
    'tgbattleship.gif':     (45, 13),
    'plbattleship.gif':     (45, 14),

    'oscarrier.gif':        (46,  1),
    'bmcarrier.gif':        (46,  2),
    'gecarrier.gif':        (46,  3),
    'yccarrier.gif':        (46,  4),
    'bhcarrier.gif':        (46,  5),
    'rfcarrier.gif':        (46,  6),
    'gscarrier.gif':        (46,  7),
    'bdcarrier.gif':        (46,  8),
    'abcarrier.gif':        (46,  9),
    'jscarrier.gif':        (46, 10),
    'cicarrier.gif':        (46, 11),
    'pccarrier.gif':        (46, 12),
    'tgcarrier.gif':        (46, 13),
    'plcarrier.gif':        (46, 14),
}


# From MAIN terrain IDs, find the offset for appropriate tile orientation based on surroundings.
AWBW_AWARENESS = {
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

    # Define which tile types MAIN terrain IDs should be aware of
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


def get_awareness_override(terr: int) -> int:
    pass
