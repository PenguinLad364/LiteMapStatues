from litemapy import Schematic, Region, BlockState
import numpy as np

from Builder import Builder

# Definition of Statue Parts
Head = Region(0, 24, 4, 10, 9, 10) # 8x8x8 Plus Padding, Loc: (0, 24, 4)
Body = Region(2, 12, 5, 6, 12, 8) # 4x12x8 Plus Padding, Loc: (2, 12, 4)
LArm = Region(2, 11, 0, 6, 14, 5) # 4x12x4 Plus Padding, Loc: (2, 12, 0)
RArm = Region(2, 11, 13, 6, 14, 5) # Loc: (2, 12, 12)
LLeg = Region(2, 0, 4, 6, 12, 5) # Loc: (2, 0, 4)
RLeg = Region(2, 0, 9, 6, 12, 5) # Loc: (2, 0, 4)

HeadBuilder = Builder(Head, [1, 0, 0, 0, 0, 0])
BodyBuilder = Builder(Body, [1, 1, 0, 0, 1, 1])
LArmBuilder = Builder(LArm, [0, 0, 0, 0, 1, 0])
RArmBuilder = Builder(RArm, [0, 1, 0, 0, 0, 0])
LLegBuilder = Builder(LLeg, [1, 0, 0, 0, 1, 1])
RLegBuilder = Builder(RLeg, [1, 1, 0, 0, 0, 1])


# Create the block state we are going to use
block1 = BlockState("minecraft:stone")
block2 = BlockState("minecraft:gold_block") 
block3 = BlockState("minecraft:diamond_block")

block_list = [block1, block2, block3]
print(block_list)

# Create an 8x8 array of random BlockState objects using object dtype
#random_blocks = np.empty((8, 8), dtype=object)
random_blocks2 = np.empty((20,20), dtype=object)

# Generate random indices for the block_set
#for i in range(8):
#    for j in range(8):
#        random_blocks[i, j] = block_list[np.random.randint(len(block_list))]

for i in range(20):
    for j in range(20):
        random_blocks2[i, j] = block_list[np.random.randint(len(block_list))]

# Print the array (for visualization)
#print(random_blocks)

HeadBuilder.BuildFace(random_blocks2)
BodyBuilder.BuildFace(random_blocks2)
LArmBuilder.BuildFace(random_blocks2)
RArmBuilder.BuildFace(random_blocks2)
LLegBuilder.BuildFace(random_blocks2)
RLegBuilder.BuildFace(random_blocks2)



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