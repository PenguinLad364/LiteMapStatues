from PIL import Image
import numpy as np

class ImageParser:
    '''
    Object used for Parsing data from Image

    Attributes:
        IMG (Image): The image we wish to process
        SizeX (int): Pixel size in X direction
        SizeY (int): Pixel size in Y direction
    '''

    def __init__(self, path):
        '''
        Initializes ImageParser object

        Parameters:
            path (str): Holds path to an image
        '''

        self.SetImage(path)

    def SetImage(self, path):
        '''
        Resets ImageParser attributes based on new image.

        Parameters:
            path (str): Holds path to an image        
        '''

        InitImage = Image.open(path)
        self.IMG = InitImage.convert('RGB')

        self.SizeX, self.SizeY = self.IMG.size

    # Returns RGB values of each pixel as an array
    def GetPixelArray(self):
        '''
        Returns the RGB values of all pixels in self.IMG

        Returns:
            OutputArray (NDArray[tuple(int)]): Holds 2D array of tuples with corresponding RGB values for each pixel
        '''

        # Load image and allocate OutputArray
        Pixels = self.IMG.load()
        OutputArray = np.empty((self.SizeX, self.SizeY), dtype = tuple)

        # Iterate through each pixel and set RGB values in output
        for i in range(self.SizeX):
            for j in range(self.SizeY):
                RBGValues = Pixels[i,j]
                OutputArray[i][j] = RBGValues
        
        return OutputArray
    
    # Returns RGB values of each pixel in a rectancular region of the image
    def GetPixelSection(self, Coord1, Coord2, Coord3, Coord4):
        '''
        Returns the RGB values of all pixels within a rectangular region in self.IMG

        Parameters:
            Coord1 (List: (int)): Represents corner of region as a coordinate (x,y)
            Coord2 (List: (int)): Represents corner of region as a coordinate (x,y)
            Coord3 (List: (int)): Represents corner of region as a coordinate (x,y)
            Coord4 (List: (int)): Represents corner of region as a coordinate (x,y)

        Returns:
            OutputArray (NDArray[tuple(int)]): Holds 2D array of tuples with corresponding RGB values for pixels within specified region
        '''

        # Define region parameters
        MinX = Coord1[0]
        MaxX = Coord2[0]
        MinY = Coord1[1]
        MaxY = Coord3[1]

        SizeX = MaxX - MinX
        SizeY = MaxY - MinY

        # Allocate OutputArray
        OutputArray = np.empty((SizeX + 1, SizeY + 1), dtype = tuple)
        OutputXCounter = 0
        OutputYCounter = 0

        Pixels = self.IMG.load()

        # Iterate through region in Image and set RGB values in output
        for i in range(MinX, MaxX + 1):
            for j in range(MinY, MaxY + 1):
                RBGValues = Pixels[i,j]
                OutputArray[OutputXCounter][OutputYCounter] = RBGValues

                OutputYCounter += 1
            OutputXCounter+= 1
            OutputYCounter = 0

        return OutputArray
    
    # Returns the average RGB values of all pixels in an image
    def GetAverageRGB(self):
        '''
        Returns the average RGB value of all pixels in self.IMG

        Returns:
            RoundedRGB (NDArray[int]): Holds the average RGB value of all pixels in self.IMG
        '''

        # Convert PixelArray to a 1-D list containing Lists of RGB values
        PixelArray = self.GetPixelArray()
        ReshapedArray = PixelArray.reshape(-1)

        # Filter transparent values
        RGBList = np.array([list(Pixel) for Pixel in ReshapedArray if list(Pixel) != [0, 0, 0]])

        # Compute Average and round RGB value
        AveragePixel = RGBList.mean(axis=0)
        RoundedRGB = np.array([int(i) for i in AveragePixel])
        
        return RoundedRGB
