class Builder:
    '''
    Represents a Builder, responsible for placing blocks inside a given region

    Attributes:
        Region (Region): Holds the region we are building in
        Padding (NDArray[int]): Holds an array of values dictating how much padding to add on each side

        CubeXMin (int): Minimum X value in our region for inner skin
        CubeXMax (int): Maximum X value in our region for inner skin
        CubeYMin (int): Minimum Y value in our region for inner skin
        CubeYMax (int): Maximum Y value in our region for inner skin
        CubeZMin (int): Minimum Z value in our region for inner skin
        CubeZMax (int): Maximum Z value in our region for inner skin

        MaskXMin (int): Minimum X value in our region for outer skin
        MaskXMax (int): Maximum X value in our region for outer skin
        MaskYMin (int): Minimum Y value in our region for outer skin
        MaskYMax (int): Maximum Y value in our region for outer skin
        MaskZMin (int): Minimum Z value in our region for outer skin
        MaskZMax (int): Maximum Z value in our region for outer skin
    '''

    def __init__(self, Region, Padding, debug = False):
        '''
        Initializes Builder object

        Parameters:
            Region (Region): Region we wish to build in
            Padding (NDArray[int]): Holds array of values used for padding to our region
            debug (bool): Used for debugging
        '''

        self.Region = Region

        # Parameters for Tracking Padding
        self.Padding = Padding

        # Parameters for Inner Cube Construction
        self.CubeYMin = Padding[0]
        self.CubeZMin = Padding[1]
        self.CubeXMin = Padding[2]
        self.CubeXMax = self.Region.maxx() - Padding[3]
        self.CubeZMax = self.Region.maxz() - Padding[4]
        self.CubeYMax = self.Region.maxy() - Padding[5]

        # Parameters for Outer Cube Construction
        self.MaskXMin = Padding[2]
        self.MaskYMin = Padding[0]
        self.MaskZMin = Padding[1]
        self.MaskXMax = self.CubeXMax + 1
        self.MaskYMax = self.CubeYMax + 1
        self.MaskZMax = self.CubeZMax + 1

        if debug == True:
            print(f"Building Cube:")
            print(f"     XMin: {self.CubeXMin}, XMax = {self.CubeXMax}")
            print(f"     YMin: {self.CubeYMin}, YMax = {self.CubeYMax}")
            print(f"     ZMin: {self.CubeZMin}, ZMax = {self.CubeZMax}")

    def BuildCube(self, FaceArray, OrderArray):
        '''
        Builds a rectangular box in our region using six Face objects in FaceArray

        Parameters:
            FaceArray (NDArray[Face]): Array of Face objects for box construction
            OrderArray (NDArray[int]): Array of integers determining which sides of the box we build first 
        '''

        # Build each face of the cube
        for i in OrderArray:
            Input = i - 1
            self.BuildFace(FaceArray[Input], Input)
            
    def BuildFace(self, Face, SideNum):
        '''
        Builds a specific side of our box from a Face object

        Parameters:
            Face (Face): Holds the Face object to build this side with
            SideNum (int): Determines what side of the box to be build
        '''

        # Get the Blocks of the Face
        Blocks = Face.BlockArray

        # Determine if we are working with a top or bottom side
        if SideNum < 3:
            TopAxis = False
        else:
            TopAxis = True

        BlocksCounterX = 0
        BlocksCounterY = 0

        # Building Sides 1 or 6
        if SideNum == 0 or SideNum == 5:
            for x in range(self.CubeXMin, self.CubeXMax + 1):
                for z in range(self.CubeZMin, self.CubeZMax + 1):
                    YIndex = self.CubeYMax if TopAxis else self.CubeYMin

                    self.Region.setblock(x, YIndex, z, Blocks[BlocksCounterX][BlocksCounterY])
                    BlocksCounterY += 1
                
                BlocksCounterX += 1
                BlocksCounterY = 0

        # Building Sides 2 or 5
        elif SideNum == 1 or SideNum == 4:
            for x in range(self.CubeXMin, self.CubeXMax + 1):
                for y in range(self.CubeYMin, self.CubeYMax + 1):
                    ZIndex = self.CubeZMax if TopAxis else self.CubeZMin

                    self.Region.setblock(x, y, ZIndex, Blocks[BlocksCounterX][BlocksCounterY])
                    BlocksCounterY += 1
                
                BlocksCounterX += 1
                BlocksCounterY = 0

        # Building Sides 3 or 4
        elif SideNum == 2 or SideNum == 3:
            for y in range(self.CubeYMin, self.CubeYMax + 1):
                for z in range(self.CubeZMin, self.CubeZMax + 1):
                    XIndex = self.CubeXMax if TopAxis else self.CubeXMin

                    self.Region.setblock(XIndex, y, z, Blocks[BlocksCounterX][BlocksCounterY])
                    BlocksCounterY += 1
                
                BlocksCounterX += 1
                BlocksCounterY = 0

    def BuildMask(self, FaceArray, OrderArray):
        '''
        Builds along the padded sides in our region using six Face objects in FaceArray

        Parameters:
            FaceArray (NDArray[Face]): Array of Face objects for box construction
            OrderArray (NDArray[int]): Array of integers determining which sides of the box we build first 
        ''' 

        # Build each face of the mask
        for i in OrderArray:
            Input = i - 1
            self.BuildMaskFace(FaceArray[Input], Input) 

    def BuildMaskFace(self, Face, SideNum):
        '''
        Builds a specific side of our padded region from a Face object

        Parameters:
            Face (Face): Holds the Face object to build this side with
            SideNum (int): Determines what side of the box to be build
        '''

        # Get blocks of Face
        Blocks = Face.BlockArray

        # Determine if we are working with a top or bottom side
        if SideNum < 3:
            TopAxis = False
        else:
            TopAxis = True

        BlocksCounterX = 0
        BlocksCounterY = 0

        # Determine if the current Side requires padding
        if self.Padding[SideNum] == 0:
            return
        else:
            # Determine what side is being worked on

            # Buidling Sides 1 or 6
            if SideNum == 0 or SideNum == 5:
                for x in range(self.MaskXMin, self.MaskXMax):
                    for z in range(self.MaskZMin, self.MaskZMax):
                        YIndex = self.Region.maxy() if TopAxis else self.Region.miny()

                        self.Region.setblock(x, YIndex, z, Blocks[BlocksCounterX][BlocksCounterY])
                        BlocksCounterY += 1
                
                    BlocksCounterX += 1
                    BlocksCounterY = 0

            # Building Sides 2 or 5
            elif SideNum == 1 or SideNum == 4:
                for x in range(self.MaskXMin, self.MaskXMax):
                    for y in range(self.MaskYMin, self.MaskYMax):
                        ZIndex = self.Region.maxz() if TopAxis else self.Region.minz()

                        self.Region.setblock(x, y, ZIndex, Blocks[BlocksCounterX][BlocksCounterY])
                        BlocksCounterY += 1

                    BlocksCounterX += 1
                    BlocksCounterY = 0
            
            # Building Sides 3 or 4
            elif SideNum == 2 or SideNum == 3:
                for y in range(self.MaskYMin, self.MaskYMax):
                    for z in range(self.MaskZMin, self.MaskZMax):
                        XIndex = self.Region.maxx() if TopAxis else self.Region.minx()

                        self.Region.setblock(XIndex, y, z, Blocks[BlocksCounterX][BlocksCounterY])
                        BlocksCounterY += 1
                    
                    BlocksCounterX += 1
                    BlocksCounterY = 0