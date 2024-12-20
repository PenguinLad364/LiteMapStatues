# Import Libraries
from litemapy import BlockState
import numpy as np
import math
import os

# Import Classes and Functions
from dict import BlockMap

# Creates a Face with a specified block
def CreatePlane(SizeX, SizeY, Block):
    '''
    Creates a 2-D array of BlockState objects, with each element being a given Block

    Parameters:
        SizeX (int): Desired size of OutputArray in X direction
        SizeY (int): Desired size of OutputArray in Y direction
        Block (BlockState): Block we wish to fill OutputArray with

    Returns:
        OutputArray (NDArray[BlockState]): Array of BlockStates
    '''

    # Allocate OutputArray
    OutputArray = np.empty((SizeX, SizeY), dtype = object)

    # Iterate through and fill OutputArray with Block
    for i in range(SizeX):
        for j in range(SizeY):
            OutputArray[i][j] = Block

    return OutputArray

# Creates a Face with a random assortment from a list of blocks
def CreateRandomPlace(SizeX, SizeY, BlockList):
    '''
    Creates a 2-D array of BlockState objects with random BlockState objects

    Parameters:
        SizeX (int): Desired size of OutputArray in X direction
        SizeY (int): Desired size of OutputArray in Y direction
        BlockList (List(BlockState)): Block we wish to fill OutputArray with

    Returns:
        OutputArray (NDArray[BlockState]): Array of BlockStates
    '''

    # Allocate OutputArray
    OutputArray = np.empty((SizeX,SizeX), dtype=object)

    # Iterate through and fill OutputArray with randomly selected BlockState object
    for i in range(SizeX):
        for j in range(SizeY):
            OutputArray[i][j] = BlockList[np.random.randint(len(BlockList))]
        
    return OutputArray

# Iterates through a folder and returns the average RGB of images in that folder
def ProcessTextures(Parser, Folder_Path):
    '''
    Iterates through a specified folder and prints the average RGB values of all png images in the folder

    Parameters: 
        Parser (ImageParser): Holds the ImageParser object used for processing
        Folder_Path (str): Holds the desired folder path
    '''

    # Iterate through all .png files
    for Img in os.listdir(Folder_Path):
        if Img.endswith('.png'):

            # Set Parser to current image
            ImgPath = os.path.join(Folder_Path, Img)
            Parser.SetImage(ImgPath)

            # Print average RGB values of image
            AvgRGB = Parser.GetAverageRGB()
            print(f"{Img[0:-4]}, {AvgRGB}")

# Calculates the different between two tuples of equal size (as Euclidean Distance)
def GetDifference(Tup1, Tup2):
    '''
    Calculates and returns the euclidean distance of equally sized tuples

    Parameters:
        Tup1 (tuple(int)): First Tuple
        Tup2 (tuple(int)): Second Tuple

    Returns:
        Dist (float): Holds euclidean distance of Tup1 and Tup2
    '''

    Dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(Tup1, Tup2)))
    return Dist

# Function that closest matching block from "BlockMap" given a tuple
def GetBlock(Input):
    '''
    Returns the value for closest matching key in BlockMap dictionary

    Parameters:
        Input (tuple(int)): Tuple we wish to map to value in BlockMap

    Returns:
        BlockString (str): Holds the value for closest matching key in BlockMap dictionary
    '''

    # Initlalze variables
    ClosestMatch = (256, 256, 256)
    LowestDiff = 10000000000000

    # Iterate through all keys in BlockMap
    for Key in BlockMap:
        Diff = GetDifference(Input, Key)

        # If conditions are met, set ClosestMatch
        if Diff < LowestDiff:
            LowestDiff = Diff
            ClosestMatch = Key

    BlockString = BlockMap[ClosestMatch]
    return BlockString


# Converts a 2-D array of RGB values to MC blocks
def ConvertToBlocks(RGBArray):
    '''
    Converts an array of RGB values to an array of corresponding BlockState objects for each entry

    Parameters:
        RGBArray (NDArray[tuple(int)]): Array of RGB values to be converted

    Returns:
        BlockArray (NDArray[BlockState]): Array of BlockState objects
    '''

    # Initialize output
    SizeX, SizeY = RGBArray.shape
    BlockArray = np.empty_like(RGBArray)

    # For each entry in RGBArray, find closest match and set in BlockArray
    for i in range(SizeX):
        for j in range(SizeY):
            CurPixel = RGBArray[i][j]
            Block = GetBlock(CurPixel)

            BlockArray[i][j] = BlockState(f"minecraft:{Block}")

    return BlockArray

