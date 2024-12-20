class Face:
    '''
    Represents some face of a box

    Attributes:
        BlockArray (NDArray[BlockState]): 
        SizeX (int): Width of our face
        SizeY (int): Height of our face
    '''

    def __init__(self, BlockArray):
        '''
        Initializes Face object

        Parameters:
            BlockArray (NDArray[BlockState]): Holds the blocks representing the Face
        '''

        self.BlockArray = BlockArray

        self.SizeX, self.SizeY = BlockArray.shape

    def SetBlocks(self, NewBlockArray):
        '''
        Resets this face's BlockArray attribute

        Parameters:
            NewBlockArray (NDArray[BlockState]): Holds the new set of blocks to represent the Face
        '''
        
        self.BlockArray = NewBlockArray

    def RotateFace(self, Rotations):
        pass

    def ReflectFace(self):
        pass