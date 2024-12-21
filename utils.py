# Import Libraries
from litemapy import BlockState
import numpy as np
import math
import os

# Import Classes and Functions
from dict import BlockMap
from Face import Face

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

def ReadSkinRegion(Parser, CoordArray):
    '''
    Reads sections of an image and outputs the corresponding blocks within Face objects

    Parameters:
        Parser (ImageParser): Parser which holds target image
        CoordArray (List[int]): Lists of coordinates for each of the 6 sides of our region
    
    Returns:
        FaceArray (NDArray[Face]): Array of Face objects
    '''
    
    FaceArray = np.empty(6, dtype = object)

    for i in range(6):
        Coord1 = CoordArray[i][0]
        Coord2 = CoordArray[i][1]
        Coord3 = CoordArray[i][2]
        Coord4 = CoordArray[1][3]

        BlockArray = ConvertToBlocks(Parser.GetPixelSection(Coord1, Coord2, Coord3, Coord4))
        FaceArray[i] = Face(BlockArray)
    
    # Necessary Rotations and Reflections
    FaceArray[0].RotateFace(1)
    FaceArray[1].RotateFace(2)
    FaceArray[2].RotateFace(1)
    FaceArray[3].RotateFace(1)
    FaceArray[4].RotateFace(2)
    FaceArray[4].ReflectFace()
    FaceArray[5].RotateFace(1)
    
    return FaceArray