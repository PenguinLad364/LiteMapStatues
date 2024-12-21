# Import Libraries
from litemapy import Schematic, Region

# Import Classes and Functions
from Builder import Builder
from ImageParser import ImageParser
from utils import ReadSkinRegion

# Define Parser for Skin Image
SkinParser = ImageParser("Target Skin.png")

# Definition of Statue Regions
Head = Region(0, 24, 4, 10, 9, 10) # 8x8x8 Plus Padding, Loc: (0, 24, 4)
Body = Region(2, 12, 5, 6, 12, 8) # 4x12x8 Plus Padding, Loc: (2, 12, 4)
LArm = Region(2, 11, 0, 6, 14, 5) # 4x12x4 Plus Padding, Loc: (2, 12, 0)
RArm = Region(2, 11, 13, 6, 14, 5) # Loc: (2, 12, 12)
LLeg = Region(2, 0, 4, 6, 12, 5) # Loc: (2, 0, 4)
RLeg = Region(2, 0, 9, 6, 12, 5) # Loc: (2, 0, 4)

# Builders which are responsible for different portions of the statue.
# Padding determines which sides need how much padding
HeadBuilder = Builder(Head, Padding = [0, 1, 1, 1, 1, 1])
BodyBuilder = Builder(Body, Padding = [0, 0, 1, 1, 0, 0])
LArmBuilder = Builder(LArm, Padding = [1, 1, 1, 1, 0, 1])
RArmBuilder = Builder(RArm, Padding = [1, 0, 1, 1, 1, 1])
LLegBuilder = Builder(LLeg, Padding = [0, 1, 1, 1, 0, 0])
RLegBuilder = Builder(RLeg, Padding = [0, 0, 1, 1, 1, 0])

# Begin Head Construction
print("Building Head")
CoordinateArray = [[[16, 0], [23, 0], [16, 7], [23, 7]],
                   [[0, 8], [7, 8], [0, 15], [7, 15]],
                   [[8, 8], [15, 8], [8, 15], [15, 15]],
                   [[24, 8], [31, 8], [24, 15], [31, 15]],
                   [[16, 8], [23, 8], [16, 15], [23, 15]],
                   [[8, 0], [15, 0], [8, 7], [15, 7]]]

HeadArray = ReadSkinRegion(SkinParser, CoordinateArray)

# Begin Body Construction
print("Building Body")
CoordinateArray = [[[28, 16], [35, 16], [28, 19], [35, 19]],
                   [[16, 20], [19, 20], [16, 31], [19, 31]],
                   [[20, 20], [27, 20], [20, 31], [27, 31]],
                   [[32, 20], [39, 20], [32, 31], [39, 31]],
                   [[28, 20], [31, 20], [28, 31], [31, 31]],
                   [[20, 16], [27, 16], [20, 19], [27, 19]]]

BodyArray = ReadSkinRegion(SkinParser, CoordinateArray)

# Begin Left Leg Construction
print("Building LLeg")
CoordinateArray = [[[8, 16], [11, 16], [8, 19], [11, 19]],
                   [[0, 20], [3, 20], [0, 31], [3, 31]],
                   [[4, 20], [7, 20], [4, 31], [7, 31]],
                   [[12, 20], [15, 20], [12, 31], [15, 31]],
                   [[8, 20], [11, 20], [8, 31], [11, 31]],
                   [[4, 16], [7, 16], [4, 19], [7, 19]]]

LLegArray = ReadSkinRegion(SkinParser, CoordinateArray)

# Begin Left Arm Construction
print("Building LArm")
CoordinateArray = [[[48, 16], [51, 16], [48, 19], [51, 19]],
                   [[40, 20], [43, 20], [40, 31], [43, 31]],
                   [[44, 20], [47, 20], [44, 31], [47, 31]],
                   [[52, 20], [55, 20], [52, 31], [55, 31]],
                   [[48, 20], [51, 20], [48, 31], [51, 31]],
                   [[44, 16], [47, 16], [44, 19], [74, 19]]]

LArmArray = ReadSkinRegion(SkinParser, CoordinateArray)

# Begin Right Leg Construction
print("Building RLeg")
CoordinateArray = [[[24, 48], [27, 48], [24, 51], [27, 51]],
                   [[16, 52], [19, 52], [16, 63], [19, 63]],
                   [[20, 52], [23, 52], [20, 63], [23, 63]],
                   [[28, 52], [31, 52], [28, 63], [31, 63]],
                   [[24, 52], [27, 52], [24, 63], [27, 63]],
                   [[20, 48], [23, 48], [20, 51], [23, 51]]]

RLegArray = ReadSkinRegion(SkinParser, CoordinateArray)

# Begin Right Arm Construction
print("Building RArm")
CoordinateArray = [[[40, 48], [43, 48], [40, 51], [43, 51]],
                   [[32, 52], [35, 52], [32, 63], [35, 63]],
                   [[36, 52], [39, 52], [36, 63], [39, 63]],
                   [[44, 52], [47, 52], [44, 63], [47, 63]],
                   [[40, 52], [43, 52], [40, 63], [43, 63]],
                   [[36, 48], [39, 48], [36, 51], [39, 51]]]

RArmArray = ReadSkinRegion(SkinParser, CoordinateArray)

# We build the Front and Back faces (3 and 4) last such that they are the last blocks placed
# We build the Top and Bottom faces (1 and 6) first such that edges are handled by subsequent faces
OrderArray = [1, 6, 2, 5, 4, 3]

HeadBuilder.BuildCube(HeadArray, OrderArray)
BodyBuilder.BuildCube(BodyArray, OrderArray)
LArmBuilder.BuildCube(LArmArray, OrderArray)
RArmBuilder.BuildCube(RArmArray, OrderArray)
LLegBuilder.BuildCube(LLegArray, OrderArray)
RLegBuilder.BuildCube(RLegArray, OrderArray)

regionDict = {"Head":Head,
              "Body":Body,
              "LArm":LArm,
              "RArm":RArm,
              "LLeg":LLeg,
              "RLeg":RLeg}

Schem = Schematic(name="Head", author="PenguinLad", description="A Head", regions=regionDict)

# Save the schematic
Schem.save("Statue.litematic")
print("Finished")