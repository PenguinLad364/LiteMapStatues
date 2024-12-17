from litemapy import Schematic, Region, BlockState
import numpy as np

class Builder:
    def __init__(self, region, Padding):
        self.Region = region

        # 1 = No Second Layer
        self.Padding = Padding

        self.XMin = self.Region.minx() + 1 - self.Padding[2]
        self.XMax = self.Region.maxx() + self.Padding[3]
        self.YMin = self.Region.miny() + 1 - self.Padding[0]
        self.YMax = self.Region.maxy() + self.Padding[5]
        self.ZMin = self.Region.minz() + 1 - self.Padding[1]
        self.ZMax = self.Region.maxz() + self.Padding[4]

        #print(f"Creating Cube with\nX: {self.XMin}")

    def BuildCube(self, block1, block2, block3):
        # First set of sides
        for x in range(self.XMin, self.XMax):
            for y in range(self.YMin, self.YMax):
                self.Region.setblock(x, y, -2, block1)
                self.Region.setblock(x, y, 1, block1)

        # Second set of sides
        #YIndicies = [self.YMax - 2, self.YMin]
        for x in range(self.XMin, self.XMax):
            for z in range(self.ZMin + 1, self.ZMax - 1):
                self.Region.setblock(x, -2, z, block2)
                self.Region.setblock(x, 1, z, block2)

        # Third set of sides
        for y in range(self.YMin + 1, self.YMax - 1):
            for z in range(self.ZMin + 1, self.ZMax - 1):
                self.Region.setblock(-2, y, z, block3)
                self.Region.setblock(1, y, z, block3)
            
    def BuildFace(self, Face):
        # First set of sides
        ZIndicies = [self.ZMax - 1, self.ZMin]
        for x in range(self.XMin, self.XMax):
            for y in range(self.YMin, self.YMax):
                i = x - 1
                j = y - 1

                self.Region.setblock(x, y, ZIndicies[0], Face[i][j])
                self.Region.setblock(x, y, ZIndicies[1], Face[i][j])

        # Second set of sides
        YIndicies = [self.YMax - 1, self.YMin]
        for x in range(self.XMin, self.XMax):
            for z in range(self.ZMin + 1, self.ZMax - 1):
                i = x - 1
                j = z - 1

                self.Region.setblock(x, YIndicies[0], z, Face[i][j])
                self.Region.setblock(x, YIndicies[1], z, Face[i][j])

        # Third set of sides
        XIndicies = [self.XMax - 1, self.XMin]
        for y in range(self.YMin + 1, self.YMax - 1):
            for z in range(self.ZMin + 1, self.ZMax - 1):
                i = y - 1
                j = z - 1

                self.Region.setblock(XIndicies[0], y, z, Face[i][j])
                self.Region.setblock(XIndicies[1], y, z, Face[i][j])