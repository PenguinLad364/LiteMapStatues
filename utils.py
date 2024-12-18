from litemapy import BlockState
import numpy as np

def CreatePlane(SizeX, SizeY, Block):
    OutputArray = np.empty((SizeX, SizeY), dtype = object)

    for i in range(SizeX):
        for j in range(SizeY):
            OutputArray[i][j] = Block

    return OutputArray

def CreateRandomPlace(SizeX, SizeY, BlockList):
    OutputArray = np.empty((SizeX,SizeX), dtype=object)

    for i in range(SizeX):
        for j in range(SizeY):
            OutputArray[i][j] = BlockList[np.random.randint(len(BlockList))]
        
    return OutputArray