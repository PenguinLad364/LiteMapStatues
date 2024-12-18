#import numpy as np

class Face:
    def __init__(self, BlockArray):
        self.BlockArray = BlockArray

        self.SizeX, self.SizeY = BlockArray.shape

    def SetBlocks(self, NewBlockArray):
        self.BlockArray = NewBlockArray

    def RotateFace(self, Rotations):
        pass

    def ReflectFace(self):
        pass