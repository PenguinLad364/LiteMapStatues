class Builder:
    def __init__(self, Region, Padding):
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
        self.MaskXMin = self.Region.minx()
        self.MaskYMin = self.Region.miny()
        self.MaskZMin = self.Region.minz()
        self.MaskXMax = self.CubeXMax + Padding[3]
        self.MaskYMax = self.CubeYMax + Padding[5]
        self.MaskZMax = self.CubeZMax + Padding[4]

    def BuildCube(self, FaceArray, OrderArray):
        # Build each face of the cube
        for i in OrderArray:
            Input = i - 1
            self.BuildFace(FaceArray[Input], Input)
            
    def BuildFace(self, Face, SideNum):
        # Get the Blocks of the Face
        Blocks = Face.BlockArray

        # Determine if we are working with a top or bottom side
        if SideNum < 3:
            TopAxis = False
        else:
            TopAxis = True

        # Building Sides 1 or 6
        if SideNum == 0 or SideNum == 5:
            for x in range(self.CubeXMin, self.CubeXMax + 1):
                for z in range(self.CubeZMin, self.CubeZMax + 1):
                    YIndex = self.CubeYMax if TopAxis else self.CubeYMin

                    self.Region.setblock(x, YIndex, z, Blocks[x - 1][z - 1])

        # Building Sides 2 or 5
        elif SideNum == 1 or SideNum == 4:
            for x in range(self.CubeXMin, self.CubeXMax + 1):
                for y in range(self.CubeYMin, self.CubeYMax + 1):
                    ZIndex = self.CubeZMax if TopAxis else self.CubeZMin

                    self.Region.setblock(x, y, ZIndex, Blocks[x - 1][y - 1])

        # Building Sides 3 or 4
        elif SideNum == 2 or SideNum == 3:
            for y in range(self.CubeYMin, self.CubeYMax + 1):
                for z in range(self.CubeZMin, self.CubeZMax + 1):
                    XIndex = self.CubeXMax if TopAxis else self.CubeXMin

                    self.Region.setblock(XIndex, y, z, Blocks[y - 1][z - 1])

    def BuildMask(self, FaceArray, OrderArray):
        # Build each face of the mask
        for i in OrderArray:
            Input = i - 1
            self.BuildMaskFace(FaceArray[Input], Input) 

    def BuildMaskFace(self, Face, SideNum):
        # Get blocks of Face
        Blocks = Face.BlockArray

        # Determine if we are working with a top or bottom side
        if SideNum < 3:
            TopAxis = False
        else:
            TopAxis = True

        # Determine if the current Side requires padding
        if self.Padding[SideNum] == 0:
            return
        else:
            # Determine what side is being worked on

            # Buidling Sides 1 or 6
            if SideNum == 0 or SideNum == 5:
                for x in range(self.MaskXMin, self.MaskXMax + 1):
                    for z in range(self.MaskZMin, self.MaskZMax + 1):
                        YIndex = self.MaskYMax if TopAxis else self.MaskYMin

                        self.Region.setblock(x, YIndex, z, Blocks[x - 1][z - 1])

            # Building Sides 2 or 5
            elif SideNum == 1 or SideNum == 4:
                for x in range(self.MaskXMin, self.MaskXMax + 1):
                    for y in range(self.MaskYMin, self.MaskYMax + 1):
                        ZIndex = self.MaskZMax if TopAxis else self.MaskZMin

                        self.Region.setblock(x, y, ZIndex, Blocks[x - 1][y - 1])
            
            # Building Sides 3 or 4
            elif SideNum == 2 or SideNum == 3:
                for y in range(self.MaskYMin, self.MaskYMax + 1):
                    for z in range(self.MaskZMin, self.MaskZMax + 1):
                        XIndex = self.MaskXMax if TopAxis else self.MaskXMin

                        self.Region.setblock(XIndex, y, z, Blocks[y - 1][z - 1])