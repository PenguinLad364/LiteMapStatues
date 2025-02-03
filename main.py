# Import Libraries
from litemapy import Schematic, Region

# Import Classes and Functions
from Builder import Builder
from ImageParser import ImageParser
from utils import ReadSkinRegion

# Define Parser for Skin Image
SkinParser = ImageParser("Target_Skin.png")

# Define whether Target Skin is a Slim or Standard model
Slim = True

# Define whether the user wishes to build second layer of skin
Second_Layer = False

# Definition of Statue Regions

# Arms are different for Slim vs Standard skins
if Slim == False:
    Head = Region(0, 24, 4, 10, 9, 10) # 8x8x8 Plus Padding, Loc: (0, 24, 4)
    Body = Region(2, 12, 5, 6, 12, 8) # 4x12x8 Plus Padding, Loc: (2, 12, 4)
    LLeg = Region(2, 0, 4, 6, 12, 5) # 4x12x4 Plus Padding, Loc: (2, 0, 4)
    RLeg = Region(2, 0, 9, 6, 12, 5) # 4x12x4 Plus Padding, Loc: (2, 0, 4)
    LArm = Region(2, 11, 0, 6, 14, 5) # 4x12x4 Plus Padding, Loc: (2, 12, 0)
    RArm = Region(2, 11, 13, 6, 14, 5) # 4x12x4 Plus Padding, Loc: (2, 12, 12)
else:
    Head = Region(0, 24, 3, 10, 9, 10) # 8x8x8 Plus Padding, Loc: (0, 24, 4)
    Body = Region(2, 12, 4, 6, 12, 8) # 4x12x8 Plus Padding, Loc: (2, 12, 4)
    LLeg = Region(2, 0, 3, 6, 12, 5) # 4x12x4 Plus Padding, Loc: (2, 0, 4)
    RLeg = Region(2, 0, 8, 6, 12, 5) # 4x12x4 Plus Padding, Loc: (2, 0, 4)
    LArm = Region(2, 11, 0, 6, 14, 4) # 3x12x4 Plus Padding, Loc: (2, 12, 0)
    RArm = Region(2, 11, 12, 6, 14, 4) # 3x12x4 Plus Padding, Loc: (2, 12, 12)

# Builders which are responsible for different portions of the statue.
# Padding determines which sides need how much padding
HeadBuilder = Builder(Head, Padding = [0, 1, 1, 1, 1, 1])
BodyBuilder = Builder(Body, Padding = [0, 0, 1, 1, 0, 0])
LArmBuilder = Builder(LArm, Padding = [1, 1, 1, 1, 0, 1])
RArmBuilder = Builder(RArm, Padding = [1, 0, 1, 1, 1, 1])
LLegBuilder = Builder(LLeg, Padding = [0, 1, 1, 1, 0, 0])
RLegBuilder = Builder(RLeg, Padding = [0, 0, 1, 1, 1, 0])

# We build the Front and Back faces (3 and 4) last such that they are the last blocks placed
# We build the Top and Bottom faces (1 and 6) first such that edges are handled by subsequent faces
OrderArray = [1, 6, 2, 5, 4, 3]

# Begin Head Construction
print("Building Head")
BaseCoordinateArray = [[[16, 0], [23, 0], [16, 7], [23, 7]],
                   [[0, 8], [7, 8], [0, 15], [7, 15]],
                   [[8, 8], [15, 8], [8, 15], [15, 15]],
                   [[24, 8], [31, 8], [24, 15], [31, 15]],
                   [[16, 8], [23, 8], [16, 15], [23, 15]],
                   [[8, 0], [15, 0], [8, 7], [15, 7]]]

HeadArray = ReadSkinRegion(SkinParser, BaseCoordinateArray)
HeadBuilder.BuildCube(HeadArray, OrderArray)

# Begin Body Construction
print("Building Body")
CoordinateArray = [[[28, 16], [35, 16], [28, 19], [35, 19]],
                   [[16, 20], [19, 20], [16, 31], [19, 31]],
                   [[20, 20], [27, 20], [20, 31], [27, 31]],
                   [[32, 20], [39, 20], [32, 31], [39, 31]],
                   [[28, 20], [31, 20], [28, 31], [31, 31]],
                   [[20, 16], [27, 16], [20, 19], [27, 19]]]

BodyArray = ReadSkinRegion(SkinParser, CoordinateArray)
BodyBuilder.BuildCube(BodyArray, OrderArray)

# Begin Left Leg Construction
print("Building LLeg")
CoordinateArray = [[[8, 16], [11, 16], [8, 19], [11, 19]],
                   [[0, 20], [3, 20], [0, 31], [3, 31]],
                   [[4, 20], [7, 20], [4, 31], [7, 31]],
                   [[12, 20], [15, 20], [12, 31], [15, 31]],
                   [[8, 20], [11, 20], [8, 31], [11, 31]],
                   [[4, 16], [7, 16], [4, 19], [7, 19]]]

LLegArray = ReadSkinRegion(SkinParser, CoordinateArray)
LLegBuilder.BuildCube(LLegArray, OrderArray)

# Begin Right Leg Construction
print("Building RLeg")
CoordinateArray = [[[24, 48], [27, 48], [24, 51], [27, 51]],
                   [[16, 52], [19, 52], [16, 63], [19, 63]],
                   [[20, 52], [23, 52], [20, 63], [23, 63]],
                   [[28, 52], [31, 52], [28, 63], [31, 63]],
                   [[24, 52], [27, 52], [24, 63], [27, 63]],
                   [[20, 48], [23, 48], [20, 51], [23, 51]]]

RLegArray = ReadSkinRegion(SkinParser, CoordinateArray)
RLegBuilder.BuildCube(RLegArray, OrderArray)

# Construct arms based on whether we have a Slim or Standard skin
if Slim == False:
    # Begin Left Arm Construction
    print("Building LArm")
    CoordinateArray = [[[48, 16], [51, 16], [48, 19], [51, 19]],
                    [[40, 20], [43, 20], [40, 31], [43, 31]],
                    [[44, 20], [47, 20], [44, 31], [47, 31]],
                    [[52, 20], [55, 20], [52, 31], [55, 31]],
                    [[48, 20], [51, 20], [48, 31], [51, 31]],
                    [[44, 16], [47, 16], [44, 19], [47, 19]]]

    LArmArray = ReadSkinRegion(SkinParser, CoordinateArray)
    LArmBuilder.BuildCube(LArmArray, OrderArray)

    # Begin Right Arm Construction
    print("Building RArm")
    CoordinateArray = [[[40, 48], [43, 48], [40, 51], [43, 51]],
                    [[32, 52], [35, 52], [32, 63], [35, 63]],
                    [[36, 52], [39, 52], [36, 63], [39, 63]],
                    [[44, 52], [47, 52], [44, 63], [47, 63]],
                    [[40, 52], [43, 52], [40, 63], [43, 63]],
                    [[36, 48], [39, 48], [36, 51], [39, 51]]]

    RArmArray = ReadSkinRegion(SkinParser, CoordinateArray)
    RArmBuilder.BuildCube(RArmArray, OrderArray)

else:
    # Begin Left Arm Construction
    print("Building LArm")
    CoordinateArray = [[[47, 16], [49, 16], [47, 19], [49, 19]],
                    [[40, 20], [43, 20], [40, 31], [43, 31]],
                    [[44, 20], [46, 20], [44, 31], [46, 31]],
                    [[51, 20], [53, 20], [51, 31], [53, 31]],
                    [[47, 20], [50, 20], [47, 31], [50, 31]],
                    [[44, 16], [46, 16], [44, 19], [46, 19]]]

    LArmArray = ReadSkinRegion(SkinParser, CoordinateArray)
    LArmBuilder.BuildCube(LArmArray, OrderArray)

    # Begin Right Arm Construction
    print("Building RArm")
    CoordinateArray = [[[39, 48], [41, 48], [39, 51], [41, 51]],
                    [[32, 52], [35, 52], [32, 63], [35, 63]],
                    [[36, 52], [38, 52], [36, 63], [38, 63]],
                    [[43, 52], [45, 52], [43, 63], [45, 63]],
                    [[39, 52], [42, 52], [39, 63], [42, 63]],
                    [[36, 48], [38, 48], [36, 51], [38, 51]]]

    RArmArray = ReadSkinRegion(SkinParser, CoordinateArray)
    RArmBuilder.BuildCube(RArmArray, OrderArray)

if Second_Layer is True:
    # Begin Head Mask Construction
    print("Building Head Mask")

    MaskCoordinateArray = [[[48, 0], [55, 0], [48, 7], [55, 7]],
                    [[32, 8], [39, 8], [32, 15], [39, 15]],
                    [[40, 8], [47, 8], [40, 15], [47, 15]],
                    [[56, 8], [63, 8], [56, 15], [63, 15]],
                    [[48, 8], [55, 8], [48, 15], [55, 15]],
                    [[40, 0], [47, 0], [40, 7], [47, 7]]]

    HeadMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
    HeadBuilder.BuildMask(HeadMaskArray, OrderArray)

    # Begin Body Mask Construction
    print("Building Body Mask")

    MaskCoordinateArray = [[[28, 32], [35, 32], [28, 35], [35, 35]],
                    [[16, 36], [19, 36], [16, 47], [19, 47]],
                    [[20, 36], [27, 36], [20, 47], [27, 47]],
                    [[32, 36], [39, 36], [32, 47], [39, 47]],
                    [[28, 36], [31, 36], [28, 47], [31, 47]],
                    [[20, 32], [27, 32], [20, 35], [27, 35]]]

    BodyMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
    BodyBuilder.BuildMask(BodyMaskArray, OrderArray)

    # Begin LLeg Mask Construction
    print("Building LLeg Mask")

    MaskCoordinateArray = [[[8, 32], [11, 32], [8, 35], [11, 35]],
                    [[0, 36], [3, 36], [0, 47], [3, 47]],
                    [[4, 36], [7, 36], [4, 47], [7, 47]],
                    [[12, 36], [15, 36], [12, 47], [15, 47]],
                    [[8, 36], [11, 36], [8, 47], [11, 47]],
                    [[4, 32], [7, 32], [4, 35], [7, 35]]]

    LLegMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
    LLegBuilder.BuildMask(LLegMaskArray, OrderArray)

    # Begin RLeg Mask Construction
    print("Building RLeg Mask")

    MaskCoordinateArray = [[[8, 48], [11, 48], [8, 51], [11, 51]],
                            [[0, 52], [3, 52], [0, 63], [3, 63]],
                            [[4, 52], [7, 52], [4, 63], [7, 63]],
                            [[12, 52], [15, 52], [12, 63], [15, 63]],
                            [[8, 52], [11, 52], [8, 63], [11, 63]],
                            [[4, 48], [7, 48], [4, 51], [7, 51]]]

    RLegMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
    RLegBuilder.BuildMask(RLegMaskArray, OrderArray)

    # Construct arms based on whether we have a Slim or Standard skin
    if Slim == False:
        # Begin Left Arm Mask Construction
        print("Building LArm Mask")
        
        MaskCoordinateArray = [[[48, 32], [51, 32], [48, 35], [51, 35]],
                                [[40, 36], [43, 36], [40, 47], [43, 47]],
                                [[44, 36], [47, 36], [44, 47], [47, 47]],
                                [[52, 36], [55, 36], [52, 47], [55, 47]],
                                [[48, 36], [51, 36], [48, 47], [51, 47]],
                                [[44, 32], [47, 32], [44, 35], [47, 35]]]

        LArmMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
        LArmBuilder.BuildMask(LArmMaskArray, OrderArray)

        # Begin Right Arm Mask Construction
        print("Building RArm Mask")
        
        MaskCoordinateArray = [[[56, 48], [59, 48], [56, 51], [59, 51]],
                            [[48, 52], [51, 52], [48, 63], [51, 63]],
                            [[52, 52], [55, 52], [52, 63], [55, 63]],
                            [[60, 52], [63, 52], [60, 63], [63, 63]],
                            [[56, 52], [59, 52], [56, 63], [59, 63]],
                            [[52, 48], [55, 48], [52, 51], [55, 51]]]

        RArmMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
        RArmBuilder.BuildMask(RArmMaskArray, OrderArray)

    else:
        # Begin Left Arm Mask Construction
        print("Building LArm Mask")

        MaskCoordinateArray = [[[47, 32], [49, 32], [47, 35], [49, 35]],
                                [[40, 36], [43, 36], [40, 47], [43, 47]],
                                [[44, 36], [46, 36], [44, 47], [46, 47]],
                                [[51, 36], [53, 36], [51, 47], [53, 47]],
                                [[47, 36], [50, 36], [47, 47], [50, 47]],
                                [[44, 32], [46, 32], [44, 35], [46, 35]]]

        LArmMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
        LArmBuilder.BuildMask(LArmMaskArray, OrderArray)

        # Begin Right Arm Mask Construction
        print("Building RArm Mask")
        
        MaskCoordinateArray = [[[55, 48], [57, 48], [55, 51], [57, 51]],
                            [[48, 52], [51, 52], [48, 63], [51, 63]],
                            [[52, 52], [54, 52], [52, 63], [54, 63]],
                            [[59, 52], [61, 52], [59, 63], [61, 63]],
                            [[55, 52], [58, 52], [55, 63], [58, 63]],
                            [[52, 48], [54, 48], [52, 51], [54, 51]]]

        RArmMaskArray = ReadSkinRegion(SkinParser, MaskCoordinateArray)
        RArmBuilder.BuildMask(RArmMaskArray, OrderArray)

regionDict = {"Head":Head,
              "Body":Body,
              "LArm":LArm,
              "RArm":RArm,
              "LLeg":LLeg,
              "RLeg":RLeg}

Schem = Schematic(name="Player Statue", author="PenguinLad", description="Player Statue", regions=regionDict)

# Save the schematic
Schem.save("Statue.litematic")
print("Finished")