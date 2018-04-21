
# TODO: Combine all properties and units in MAIN with a key for country?
# TODO: This module is going to need some refactoring to account for IDs present in one format and not another.

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

    161:    "RFHQ",
    162:    "RFCity",
    163:    "RFBase",
    164:    "RFAirport",
    165:    "RFSeaport",
    166:    "RFTower",
    167:    "RFLab",

    171:    "GSHQ",
    172:    "GSCity",
    173:    "GSBase",
    174:    "GSAirport",
    175:    "GSSeaport",
    176:    "GSTower",
    177:    "GSLab",

    181:    "BDHQ",
    182:    "BDCity",
    183:    "BDBase",
    184:    "BDAirport",
    185:    "BDSeaport",
    186:    "BDTower",
    187:    "BDLab",

    191:    "ABHQ",
    192:    "ABCity",
    193:    "ABBase",
    194:    "ABAirport",
    195:    "ABSeaport",
    196:    "ABTower",
    197:    "ABLab",

    201:    "JSHQ",
    202:    "JSCity",
    203:    "JSBase",
    204:    "JSAirport",
    205:    "JSSeaport",
    206:    "JSTower",
    207:    "JSLab",

    211:    "CIHQ",
    212:    "CICity",
    213:    "CIBase",
    214:    "CIAirport",
    215:    "CISeaport",
    216:    "CITower",
    217:    "CILab",

    221:    "PCHQ",
    222:    "PCCity",
    223:    "PCBase",
    224:    "PCAirport",
    225:    "PCSeaport",
    226:    "PCTower",
    227:    "PCLab",

    231:    "TGHQ",
    232:    "TGCity",
    233:    "TGBase",
    234:    "TGAirport",
    235:    "TGSeaport",
    236:    "TGTower",
    237:    "TGLab",

    241:    "PLHQ",
    242:    "PLCity",
    243:    "PLBase",
    244:    "PLAirport",
    245:    "PLSeaport",
    246:    "PLTower",
    247:    "PLLab",

    # 251:    "TBDHQ",
    # 252:    "TBDCity",
    # 253:    "TBDBase",
    # 254:    "TBDAirport",
    # 255:    "TBDSeaport",
    # 256:    "TBDTower",
    # 257:    "TBDLab",

    # 261:    "TBDHQ",
    # 262:    "TBDCity",
    # 263:    "TBDBase",
    # 264:    "TBDAirport",
    # 265:    "TBDSeaport",
    # 266:    "TBDTower",
    # 267:    "TBDLab",

    # 271:    "TBDHQ",
    # 272:    "TBDCity",
    # 273:    "TBDBase",
    # 274:    "TBDAirport",
    # 275:    "TBDSeaport",
    # 276:    "TBDTower",
    # 277:    "TBDLab",

    # 281:    "TBDHQ",
    # 282:    "TBDCity",
    # 283:    "TBDBase",
    # 284:    "TBDAirport",
    # 285:    "TBDSeaport",
    # 286:    "TBDTower",
    # 287:    "TBDLab",

    # 291:    "TBDHQ",
    # 292:    "TBDCity",
    # 293:    "TBDBase",
    # 294:    "TBDAirport",
    # 295:    "TBDSeaport",
    # 296:    "TBDTower",
    # 297:    "TBDLab",

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
    6:      "Red Fire",
    7:      "Grey Sky",
    8:      "Brown Desert",
    9:      "Amber Blaze",
    10:      "Jade Sun",
    11:     "Cobalt Ice",
    12:     "Pink Cosmos",
    13:     "Teal Galaxy",
    14:     "Purple Lightning",
    # 15:     "TBD",
    # 16:     "TBD",
    # 17:     "TBD",
    # 18:     "TBD",
    # 19:     "TBD",
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

    601:    "RFInfantry",
    602:    "RFMech",
    611:    "RFAPC",
    612:    "RFRecon",
    613:    "RFTank",
    614:    "RFMDTank",
    615:    "RFNeotank",
    616:    "RFMegatank",
    617:    "RFAntiAir",
    621:    "RFArtillery",
    622:    "RFRocket",
    623:    "RFMissile",
    624:    "RFPipeRunner",
    625:    "RFOozium",
    631:    "RFTCopter",
    632:    "RFBCopter",
    633:    "RFFighter",
    634:    "RFBomber",
    635:    "RFStealth",
    636:    "RFBBomb",
    641:    "RFBBoat",
    642:    "RFLander",
    643:    "RFCruiser",
    644:    "RFSubmarine",
    645:    "RFBattleship",
    646:    "RFCarrier",

    701:    "GSInfantry",
    702:    "GSMech",
    711:    "GSAPC",
    712:    "GSRecon",
    713:    "GSTank",
    714:    "GSMDTank",
    715:    "GSNeotank",
    716:    "GSMegatank",
    717:    "GSAntiAir",
    721:    "GSArtillery",
    722:    "GSRocket",
    723:    "GSMissile",
    724:    "GSPipeRunner",
    725:    "GSOozium",
    731:    "GSTCopter",
    732:    "GSBCopter",
    733:    "GSFighter",
    734:    "GSBomber",
    735:    "GSStealth",
    736:    "GSBBomb",
    741:    "GSBBoat",
    742:    "GSLander",
    743:    "GSCruiser",
    744:    "GSSubmarine",
    745:    "GSBattleship",
    746:    "GSCarrier",

    801:    "BDInfantry",
    802:    "BDMech",
    811:    "BDAPC",
    812:    "BDRecon",
    813:    "BDTank",
    814:    "BDMDTank",
    815:    "BDNeotank",
    816:    "BDMegatank",
    817:    "BDAntiAir",
    821:    "BDArtillery",
    822:    "BDRocket",
    823:    "BDMissile",
    824:    "BDPipeRunner",
    825:    "BDOozium",
    831:    "BDTCopter",
    832:    "BDBCopter",
    833:    "BDFighter",
    834:    "BDBomber",
    835:    "BDStealth",
    836:    "BDBBomb",
    841:    "BDBBoat",
    842:    "BDLander",
    843:    "BDCruiser",
    844:    "BDSubmarine",
    845:    "BDBattleship",
    846:    "BDCarrier",

    901:    "ABInfantry",
    902:    "ABMech",
    911:    "ABAPC",
    912:    "ABRecon",
    913:    "ABTank",
    914:    "ABMDTank",
    915:    "ABNeotank",
    916:    "ABMegatank",
    917:    "ABAntiAir",
    921:    "ABArtillery",
    922:    "ABRocket",
    923:    "ABMissile",
    924:    "ABPipeRunner",
    925:    "ABOozium",
    931:    "ABTCopter",
    932:    "ABBCopter",
    933:    "ABFighter",
    934:    "ABBomber",
    935:    "ABStealth",
    936:    "ABBBomb",
    941:    "ABBBoat",
    942:    "ABLander",
    943:    "ABCruiser",
    944:    "ABSubmarine",
    945:    "ABBattleship",
    946:    "ABCarrier",

    1001:   "JSInfantry",
    1002:   "JSMech",
    1011:   "JSAPC",
    1012:   "JSRecon",
    1013:   "JSTank",
    1014:   "JSMDTank",
    1015:   "JSNeotank",
    1016:   "JSMegatank",
    1017:   "JSAntiAir",
    1021:   "JSArtillery",
    1022:   "JSRocket",
    1023:   "JSMissile",
    1024:   "JSPipeRunner",
    1025:   "JSOozium",
    1031:   "JSTCopter",
    1032:   "JSBCopter",
    1033:   "JSFighter",
    1034:   "JSBomber",
    1035:   "JSStealth",
    1036:   "JSBBomb",
    1041:   "JSBBoat",
    1042:   "JSLander",
    1043:   "JSCruiser",
    1044:   "JSSubmarine",
    1045:   "JSBattleship",
    1046:   "JSCarrier",

    1101:   "CIInfantry",
    1102:   "CIMech",
    1111:   "CIAPC",
    1112:   "CIRecon",
    1113:   "CITank",
    1114:   "CIMDTank",
    1115:   "CINeotank",
    1116:   "CIMegatank",
    1117:   "CIAntiAir",
    1121:   "CIArtillery",
    1122:   "CIRocket",
    1123:   "CIMissile",
    1124:   "CIPipeRunner",
    1125:   "CIOozium",
    1131:   "CITCopter",
    1132:   "CIBCopter",
    1133:   "CIFighter",
    1134:   "CIBomber",
    1135:   "CIStealth",
    1136:   "CIBBomb",
    1141:   "CIBBoat",
    1142:   "CILander",
    1143:   "CICruiser",
    1144:   "CISubmarine",
    1145:   "CIBattleship",
    1146:   "CICarrier",

    1201:   "PCInfantry",
    1202:   "PCMech",
    1211:   "PCAPC",
    1212:   "PCRecon",
    1213:   "PCTank",
    1214:   "PCMDTank",
    1215:   "PCNeotank",
    1216:   "PCMegatank",
    1217:   "PCAntiAir",
    1221:   "PCArtillery",
    1222:   "PCRocket",
    1223:   "PCMissile",
    1224:   "PCPipeRunner",
    1225:   "PCOozium",
    1231:   "PCTCopter",
    1232:   "PCBCopter",
    1233:   "PCFighter",
    1234:   "PCBomber",
    1235:   "PCStealth",
    1236:   "PCBBomb",
    1241:   "PCBBoat",
    1242:   "PCLander",
    1243:   "PCCruiser",
    1244:   "PCSubmarine",
    1245:   "PCBattleship",
    1246:   "PCCarrier",

    1301:   "TGInfantry",
    1302:   "TGMech",
    1311:   "TGAPC",
    1312:   "TGRecon",
    1313:   "TGTank",
    1314:   "TGMDTank",
    1315:   "TGNeotank",
    1316:   "TGMegatank",
    1317:   "TGAntiAir",
    1321:   "TGArtillery",
    1322:   "TGRocket",
    1323:   "TGMissile",
    1324:   "TGPipeRunner",
    1325:   "TGOozium",
    1331:   "TGTCopter",
    1332:   "TGBCopter",
    1333:   "TGFighter",
    1334:   "TGBomber",
    1335:   "TGStealth",
    1336:   "TGBBomb",
    1341:   "TGBBoat",
    1342:   "TGLander",
    1343:   "TGCruiser",
    1344:   "TGSubmarine",
    1345:   "TGBattleship",
    1346:   "TGCarrier",

    1401:   "PLInfantry",
    1402:   "PLMech",
    1411:   "PLAPC",
    1412:   "PLRecon",
    1413:   "PLTank",
    1414:   "PLMDTank",
    1415:   "PLNeotank",
    1416:   "PLMegatank",
    1417:   "PLAntiAir",
    1421:   "PLArtillery",
    1422:   "PLRocket",
    1423:   "PLMissile",
    1424:   "PLPipeRunner",
    1425:   "PLOozium",
    1431:   "PLTCopter",
    1432:   "PLBCopter",
    1433:   "PLFighter",
    1434:   "PLBomber",
    1435:   "PLStealth",
    1436:   "PLBBomb",
    1441:   "PLBBoat",
    1442:   "PLLander",
    1443:   "PLCruiser",
    1444:   "PLSubmarine",
    1445:   "PLBattleship",
    1446:   "PLCarrier",
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
    65535:  0,     # Empty

    500:    101,   # OSInfantry
    520:    102,   # OSMech
    522:    111,   # OSAPC
    502:    112,   # OSRecon
    521:    113,   # OSTank
    501:    114,   # OSMDTank
    509:    115,   # OSNeotank
    510:    116,   # OSMegatank
    504:    117,   # OSAntiAir
    503:    121,   # OSArtillery
    523:    122,   # OSRocket
    524:    123,   # OSMissile
    511:    124,   # OSPipeRunner
    512:    125,   # OSOozium
    526:    131,   # OSTCopter
    506:    132,   # OSBCopter
    505:    133,   # OSFighter
    525:    134,   # OSBomber
    531:    135,   # OSStealth
    532:    136,   # OSBBomb
    529:    141,   # OSBBoat
    508:    142,   # OSLander
    527:    143,   # OSCruiser
    528:    144,   # OSSubmarine
    507:    145,   # OSBattleship
    530:    146,   # OSCarrier

    540:    201,   # BMInfantry
    560:    202,   # BMMech
    562:    211,   # BMAPC
    542:    212,   # BMRecon
    561:    213,   # BMTank
    541:    214,   # BMMDTank
    549:    215,   # BMNeotank
    550:    216,   # BMMegatank
    544:    217,   # BMAntiAir
    543:    221,   # BMArtillery
    563:    222,   # BMRocket
    564:    223,   # BMMissile
    551:    224,   # BMPipeRunner
    552:    225,   # BMOozium
    566:    231,   # BMTCopter
    546:    232,   # BMBCopter
    545:    233,   # BMFighter
    565:    234,   # BMBomber
    571:    235,   # BMStealth
    572:    236,   # BMBBomb
    569:    241,   # BMBBoat
    548:    242,   # BMLander
    567:    243,   # BMCruiser
    568:    244,   # BMSubmarine
    547:    245,   # BMBattleship
    570:    246,   # BMCarrier

    580:    301,   # GEInfantry
    600:    302,   # GEMech
    602:    311,   # GEAPC
    582:    312,   # GERecon
    601:    313,   # GETank
    581:    314,   # GEMDTank
    589:    315,   # GENeotank
    590:    316,   # GEMegatank
    584:    317,   # GEAntiAir
    583:    321,   # GEArtillery
    603:    322,   # GERocket
    604:    323,   # GEMissile
    591:    324,   # GEPipeRunner
    592:    325,   # GEOozium
    606:    331,   # GETCopter
    586:    332,   # GEBCopter
    585:    333,   # GEFighter
    605:    334,   # GEBomber
    611:    335,   # GEStealth
    612:    336,   # GEBBomb
    609:    341,   # GEBBoat
    588:    342,   # GELander
    607:    343,   # GECruiser
    608:    344,   # GESubmarine
    587:    345,   # GEBattleship
    610:    346,   # GECarrier

    620:    401,   # YCInfantry
    640:    402,   # YCMech
    642:    411,   # YCAPC
    622:    412,   # YCRecon
    641:    413,   # YCTank
    621:    414,   # YCMDTank
    629:    415,   # YCNeotank
    630:    416,   # YCMegatank
    624:    417,   # YCAntiAir
    623:    421,   # YCArtillery
    643:    422,   # YCRocket
    644:    423,   # YCMissile
    631:    424,   # YCPipeRunner
    632:    425,   # YCOozium
    646:    431,   # YCTCopter
    626:    432,   # YCBCopter
    625:    433,   # YCFighter
    645:    434,   # YCBomber
    651:    435,   # YCStealth
    652:    436,   # YCBBomb
    649:    441,   # YCBBoat
    628:    442,   # YCLander
    647:    443,   # YCCruiser
    648:    444,   # YCSubmarine
    627:    445,   # YCBattleship
    650:    446,   # YCCarrier

    660:    501,   # BHInfantry
    680:    502,   # BHMech
    682:    511,   # BHAPC
    662:    512,   # BHRecon
    681:    513,   # BHTank
    661:    514,   # BHMDTank
    669:    515,   # BHNeotank
    670:    516,   # BHMegatank
    664:    517,   # BHAntiAir
    663:    521,   # BHArtillery
    683:    522,   # BHRocket
    684:    523,   # BHMissile
    671:    524,   # BHPipeRunner
    672:    525,   # BHOozium
    686:    531,   # BHTCopter
    666:    532,   # BHBCopter
    665:    533,   # BHFighter
    685:    534,   # BHBomber
    691:    535,   # BHStealth
    692:    536,   # BHBBomb
    689:    541,   # BHBBoat
    668:    542,   # BHLander
    687:    543,   # BHCruiser
    688:    544,   # BHSubmarine
    667:    545,   # BHBattleship
    690:    546,   # BHCarrier
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
for k, v in MAIN_UNIT_TO_AWS.items():
    if len(v) == 0:
        MAIN_UNIT_TO_AWS[k] = [65535]

# print(MAIN_UNIT_TO_AWS)

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
    81:     162,  # Red Fire City
    82:     163,  # Red Fire Base
    83:     164,  # Red Fire Airport
    84:     165,  # Red Fire Port
    85:     161,  # Red Fire HQ
    86:     172,  # Grey Sky City
    87:     173,  # Grey Sky Base
    88:     174,  # Grey Sky Airport
    89:     175,  # Grey Sky Port
    90:     171,  # Grey Sky HQ
    91:     152,  # Black Hole City
    92:     153,  # Black Hole Base
    93:     154,  # Black Hole Airport
    94:     155,  # Black Hole Port
    95:     151,  # Black Hole HQ
    96:     182,  # Brown Desert City
    97:     183,  # Brown Desert Base
    98:     184,  # Brown Desert Airport
    99:     185,  # Brown Desert Port
    100:    181,  # Brown Desert HQ
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
    117:    194,  # Amber Blaze Airport
    118:    193,  # Amber Blaze Base
    119:    192,  # Amber Blaze City
    120:    191,  # Amber Blaze HQ
    121:    195,  # Amber Blaze Port
    122:    204,  # Jade Sun Airport
    123:    203,  # Jade Sun Base
    124:    202,  # Jade Sun City
    125:    201,  # Jade Sun HQ
    126:    205,  # Jade Sun Port
    127:    196,  # Amber Blaze Com Tower
    128:    156,  # Black Hole Com Tower
    129:    126,  # Blue Moon Com Tower
    130:    186,  # Brown Desert Com Tower
    131:    136,  # Green Earth Com Tower
    132:    206,  # Jade Sun Com Tower
    133:    106,  # Neutral Com Tower
    134:    116,  # Orange Star Com Tower
    135:    166,  # Red Fire Com Tower
    136:    146,  # Yellow Comet Com Tower
    137:    176,  # Grey Sky Com Tower
    138:    197,  # Amber Blaze Lab
    139:    157,  # Black Hole Lab
    140:    127,  # Blue Moon Lab
    141:    187,  # Brown Desert Lab
    142:    137,  # Green Earth Lab
    143:    177,  # Grey Sky Lab
    144:    207,  # Jade Sun Lab
    145:    107,  # Neutral Lab
    146:    117,  # Orange Star Lab
    147:    167,  # Red Fire Lab
    148:    147,  # Yellow Comet Lab
    149:    214,  # Cobalt Ice Airport
    150:    213,  # Cobalt Ice Base
    151:    212,  # Cobalt Ice City
    152:    216,  # Cobalt Ice Com Tower
    153:    211,  # Cobalt Ice HQ
    154:    217,  # Cobalt Ice Lab
    155:    215,  # Cobalt Ice Port
    156:    224,  # Pink Cosmos Airport
    157:    223,  # Pink Cosmos Base
    158:    222,  # Pink Cosmos City
    159:    226,  # Pink Cosmos Com Tower
    160:    221,  # Pink Cosmos HQ
    161:    227,  # Pink Cosmos Lab
    162:    225,  # Pink Cosmos Port
    163:    234,  # Teal Galaxy Airport
    164:    233,  # Teal Galaxy Base
    165:    232,  # Teal Galaxy City
    166:    236,  # Teal Galaxy Com Tower
    167:    231,  # Teal Galaxy HQ
    168:    237,  # Teal Galaxy Lab
    169:    235,  # Teal Galaxy Port
    170:    244,  # Purple Lightning Airport
    171:    243,  # Purple Lightning Base
    172:    242,  # Purple Lightning City
    173:    246,  # Purple Lightning Com Tower
    174:    241,  # Purple Lightning HQ
    175:    247,  # Purple Lightning Lab
    176:    245,  # Purple Lightning Port
}

AWBW_UNIT_SPRITE = {
    'osinfantry':        101,
    'bminfantry':        201,
    'geinfantry':        301,
    'ycinfantry':        401,
    'bhinfantry':        501,
    'rfinfantry':        601,
    'gsinfantry':        701,
    'bdinfantry':        801,
    'abinfantry':        901,
    'jsinfantry':       1001,
    'ciinfantry':       1101,
    'pcinfantry':       1201,
    'tginfantry':       1301,
    'plinfantry':       1401,

    'osmech':            102,
    'bmmech':            202,
    'gemech':            302,
    'ycmech':            402,
    'bhmech':            502,
    'rfmech':            602,
    'gsmech':            702,
    'bdmech':            802,
    'abmech':            902,
    'jsmech':           1002,
    'cimech':           1102,
    'pcmech':           1202,
    'tgmech':           1302,
    'plmech':           1402,

    'osapc':             111,
    'bmapc':             211,
    'geapc':             311,
    'ycapc':             411,
    'bhapc':             511,
    'rfapc':             611,
    'gsapc':             711,
    'bdapc':             811,
    'abapc':             911,
    'jsapc':            1011,
    'ciapc':            1111,
    'pcapc':            1211,
    'tgapc':            1311,
    'plapc':            1411,

    'osrecon':           112,
    'bmrecon':           212,
    'gerecon':           312,
    'ycrecon':           412,
    'bhrecon':           512,
    'rfrecon':           612,
    'gsrecon':           712,
    'bdrecon':           812,
    'abrecon':           912,
    'jsrecon':          1012,
    'cirecon':          1112,
    'pcrecon':          1212,
    'tgrecon':          1312,
    'plrecon':          1412,

    'ostank':            113,
    'bmtank':            213,
    'getank':            313,
    'yctank':            413,
    'bhtank':            513,
    'rftank':            613,
    'gstank':            713,
    'bdtank':            813,
    'abtank':            913,
    'jstank':           1013,
    'citank':           1113,
    'pctank':           1213,
    'tgtank':           1313,
    'pltank':           1413,

    'osmd.tank':         114,
    'bmmd.tank':         214,
    'gemd.tank':         314,
    'ycmd.tank':         414,
    'bhmd.tank':         514,
    'rfmd.tank':         614,
    'gsmd.tank':         714,
    'bdmd.tank':         814,
    'abmd.tank':         914,
    'jsmd.tank':        1014,
    'cimd.tank':        1114,
    'pcmd.tank':        1214,
    'tgmd.tank':        1314,
    'plmd.tank':        1414,

    'osneotank':         115,
    'bmneotank':         215,
    'geneotank':         315,
    'ycneotank':         415,
    'bhneotank':         515,
    'rfneotank':         615,
    'gsneotank':         715,
    'bdneotank':         815,
    'abneotank':         915,
    'jsneotank':        1015,
    'cineotank':        1115,
    'pcneotank':        1215,
    'tgneotank':        1315,
    'plneotank':        1415,

    'osmegatank':        116,
    'bmmegatank':        216,
    'gemegatank':        316,
    'ycmegatank':        416,
    'bhmegatank':        516,
    'rfmegatank':        616,
    'gsmegatank':        716,
    'bdmegatank':        816,
    'abmegatank':        916,
    'jsmegatank':       1016,
    'cimegatank':       1116,
    'pcmegatank':       1216,
    'tgmegatank':       1316,
    'plmegatank':       1416,

    'osanti-air':        117,
    'bmanti-air':        217,
    'geanti-air':        317,
    'ycanti-air':        417,
    'bhanti-air':        517,
    'rfanti-air':        617,
    'gsanti-air':        717,
    'bdanti-air':        817,
    'abanti-air':        917,
    'jsanti-air':       1017,
    'cianti-air':       1117,
    'pcanti-air':       1217,
    'tganti-air':       1317,
    'planti-air':       1417,

    'osartillery':       121,
    'bmartillery':       221,
    'geartillery':       321,
    'ycartillery':       421,
    'bhartillery':       521,
    'rfartillery':       621,
    'gsartillery':       721,
    'bdartillery':       821,
    'abartillery':       921,
    'jsartillery':      1021,
    'ciartillery':      1121,
    'pcartillery':      1221,
    'tgartillery':      1321,
    'plartillery':      1421,

    'osrocket':          122,
    'bmrocket':          222,
    'gerocket':          322,
    'ycrocket':          422,
    'bhrocket':          522,
    'rfrocket':          622,
    'gsrocket':          722,
    'bdrocket':          822,
    'abrocket':          922,
    'jsrocket':         1022,
    'cirocket':         1122,
    'pcrocket':         1222,
    'tgrocket':         1322,
    'plrocket':         1422,

    'osmissile':         123,
    'bmmissile':         223,
    'gemissile':         323,
    'ycmissile':         423,
    'bhmissile':         523,
    'rfmissile':         623,
    'gsmissile':         723,
    'bdmissile':         823,
    'abmissile':         923,
    'jsmissile':        1023,
    'cimissile':        1123,
    'pcmissile':        1223,
    'tgmissile':        1323,
    'plmissile':        1423,

    'ospiperunner':      124,
    'bmpiperunner':      224,
    'gepiperunner':      324,
    'ycpiperunner':      424,
    'bhpiperunner':      524,
    'rfpiperunner':      624,
    'gspiperunner':      724,
    'bdpiperunner':      824,
    'abpiperunner':      924,
    'jspiperunner':     1024,
    'cipiperunner':     1124,
    'pcpiperunner':     1224,
    'tgpiperunner':     1324,
    'plpiperunner':     1424,

    'ost-copter':        131,
    'bmt-copter':        231,
    'get-copter':        331,
    'yct-copter':        431,
    'bht-copter':        531,
    'rft-copter':        631,
    'gst-copter':        731,
    'bdt-copter':        831,
    'abt-copter':        931,
    'jst-copter':       1031,
    'cit-copter':       1131,
    'pct-copter':       1231,
    'tgt-copter':       1331,
    'plt-copter':       1431,

    'osb-copter':        132,
    'bmb-copter':        232,
    'geb-copter':        332,
    'ycb-copter':        432,
    'bhb-copter':        532,
    'rfb-copter':        632,
    'gsb-copter':        732,
    'bdb-copter':        832,
    'abb-copter':        932,
    'jsb-copter':       1032,
    'cib-copter':       1132,
    'pcb-copter':       1232,
    'tgb-copter':       1332,
    'plb-copter':       1432,

    'osfighter':         133,
    'bmfighter':         233,
    'gefighter':         333,
    'ycfighter':         433,
    'bhfighter':         533,
    'rffighter':         633,
    'gsfighter':         733,
    'bdfighter':         833,
    'abfighter':         933,
    'jsfighter':        1033,
    'cifighter':        1133,
    'pcfighter':        1233,
    'tgfighter':        1333,
    'plfighter':        1433,

    'osbomber':          134,
    'bmbomber':          234,
    'gebomber':          334,
    'ycbomber':          434,
    'bhbomber':          534,
    'rfbomber':          634,
    'gsbomber':          734,
    'bdbomber':          834,
    'abbomber':          934,
    'jsbomber':         1034,
    'cibomber':         1134,
    'pcbomber':         1234,
    'tgbomber':         1334,
    'plbomber':         1434,

    'osstealth':         135,
    'bmstealth':         235,
    'gestealth':         335,
    'ycstealth':         435,
    'bhstealth':         535,
    'rfstealth':         635,
    'gsstealth':         735,
    'bdstealth':         835,
    'abstealth':         935,
    'jsstealth':        1035,
    'cistealth':        1135,
    'pcstealth':        1235,
    'tgstealth':        1335,
    'plstealth':        1435,

    'osblackbomb':       136,
    'bmblackbomb':       236,
    'geblackbomb':       336,
    'ycblackbomb':       436,
    'bhblackbomb':       536,
    'rfblackbomb':       636,
    'gsblackbomb':       736,
    'bdblackbomb':       836,
    'abblackbomb':       936,
    'jsblackbomb':      1036,
    'ciblackbomb':      1136,
    'pcblackbomb':      1236,
    'tgblackbomb':      1336,
    'plblackbomb':      1436,

    'osblackboat':       141,
    'bmblackboat':       241,
    'geblackboat':       341,
    'ycblackboat':       441,
    'bhblackboat':       541,
    'rfblackboat':       641,
    'gsblackboat':       741,
    'bdblackboat':       841,
    'abblackboat':       941,
    'jsblackboat':      1041,
    'ciblackboat':      1141,
    'pcblackboat':      1241,
    'tgblackboat':      1341,
    'plblackboat':      1441,

    'oslander':          142,
    'bmlander':          242,
    'gelander':          342,
    'yclander':          442,
    'bhlander':          542,
    'rflander':          642,
    'gslander':          742,
    'bdlander':          842,
    'ablander':          942,
    'jslander':         1042,
    'cilander':         1142,
    'pclander':         1242,
    'tglander':         1342,
    'pllander':         1442,

    'oscruiser':         143,
    'bmcruiser':         243,
    'gecruiser':         343,
    'yccruiser':         443,
    'bhcruiser':         543,
    'rfcruiser':         643,
    'gscruiser':         743,
    'bdcruiser':         843,
    'abcruiser':         943,
    'jscruiser':        1043,
    'cicruiser':        1143,
    'pccruiser':        1243,
    'tgcruiser':        1343,
    'plcruiser':        1443,

    'ossub':             144,
    'bmsub':             244,
    'gesub':             344,
    'ycsub':             444,
    'bhsub':             544,
    'rfsub':             644,
    'gssub':             744,
    'bdsub':             844,
    'absub':             944,
    'jssub':            1044,
    'cisub':            1144,
    'pcsub':            1244,
    'tgsub':            1344,
    'plsub':            1444,

    'osbattleship':      145,
    'bmbattleship':      245,
    'gebattleship':      345,
    'ycbattleship':      445,
    'bhbattleship':      545,
    'rfbattleship':      645,
    'gsbattleship':      745,
    'bdbattleship':      845,
    'abbattleship':      945,
    'jsbattleship':     1045,
    'cibattleship':     1145,
    'pcbattleship':     1245,
    'tgbattleship':     1345,
    'plbattleship':     1445,

    'oscarrier':         146,
    'bmcarrier':         246,
    'gecarrier':         346,
    'yccarrier':         446,
    'bhcarrier':         546,
    'rfcarrier':         646,
    'gscarrier':         746,
    'bdcarrier':         846,
    'abcarrier':         946,
    'jscarrier':        1046,
    'cicarrier':        1146,
    'pccarrier':        1246,
    'tgcarrier':        1346,
    'plcarrier':        1446
}

# Relate MAIN IDs to AWBW IDs
MAIN_TERR_TO_AWBW = {k: [x for x in AWBW_TERR.keys() if AWBW_TERR.get(x, None) == k]
                     for k in MAIN_TERR.keys()}
MAIN_TERR_TO_AWBW[999] = [""]
for k, v in MAIN_TERR_TO_AWBW.items():  # Non-AWBW tiles become warp-tiles
    if len(v) == 0:
        MAIN_TERR_TO_AWBW[k] = [""]

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
