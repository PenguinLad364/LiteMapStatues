# Import Libraries
from litemapy import Schematic, Region, BlockState
import numpy as np

# Import Classes and Functions
from Builder import Builder
from Face import Face
from ImageParser import ImageParser
from utils import CreatePlane, ConvertToBlocks, ReadSkinRegion

# Define Parser for Skin Image
SkinParser = ImageParser("RandomSkin.png")

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
CoordinateArray = [[[16, 0], [23, 0], [16, 7], [23, 7]],
                   [[0, 8], [7, 8], [0, 15], [7, 15]],
                   [[8, 8], [15, 8], [8, 15], [15, 15]],
                   [[24, 8], [31, 8], [24, 15], [31, 15]],
                   [[16, 8], [23, 8], [16, 15], [23, 15]],
                   [[8, 0], [15, 0], [8, 7], [15, 7]]]

HeadArray = ReadSkinRegion(SkinParser, CoordinateArray)

HeadArray[0].RotateFace(1)
HeadArray[1].RotateFace(2)
HeadArray[2].RotateFace(1)
HeadArray[3].RotateFace(1)
HeadArray[4].RotateFace(2)
HeadArray[4].ReflectFace()
HeadArray[5].RotateFace(2)

# Create the block states we are going to use
block1 = BlockState("minecraft:redstone_block")
block2 = BlockState("minecraft:gold_block") 
block3 = BlockState("minecraft:diamond_block")
block4 = BlockState("minecraft:copper_block")
block5 = BlockState("minecraft:iron_block")
block6 = BlockState("minecraft:coal_block")

block7 = BlockState("minecraft:honey_block")

# Create 6 different faces for testing
Face1 = Face(CreatePlane(20, 20, block1))
Face2 = Face(CreatePlane(20, 20, block2))
Face3 = Face(CreatePlane(20, 20, block3))
Face4 = Face(CreatePlane(20, 20, block4))
Face5 = Face(CreatePlane(20, 20, block5))
Face6 = Face(CreatePlane(20, 20, block6))

FaceArray = np.array([Face1, Face2, Face3, Face4, Face5, Face6], dtype = object)

# We build the Front and Back faces (3 and 4) last such that they are the last blocks placed
# We build the Top and Bottom faces (1 and 6) first such that edges are handled by subsequent faces
OrderArray = [1, 6, 2, 5, 4, 3]

BodyBuilder.BuildCube(FaceArray, OrderArray)
HeadBuilder.BuildCube(HeadArray, OrderArray)
LArmBuilder.BuildCube(FaceArray, OrderArray)
RArmBuilder.BuildCube(FaceArray, OrderArray)
LLegBuilder.BuildCube(FaceArray, OrderArray)
RLegBuilder.BuildCube(FaceArray, OrderArray)

regionDict = {"Head":Head,
              "Body":Body,
              "LArm":LArm,
              "RArm":RArm,
              "LLeg":LLeg,
              "RLeg":RLeg}

Schem = Schematic(name="Head", author="PenguinLad", description="A Head", regions=regionDict)

# Save the schematic
Schem.save("planet.litematic")
print("Finished")