# 12/17/24 Version 0.1
## Repo Publication

- Added "Builder" Class
- Successfully creates Litematica Statue with random block palette

# 12/17/24 Version 0.2

- Renamed "test.py" to "main.py"
- Added ChangeLog.md
- Updated .gitignore

- Removed unneccessary comments from "main.py" and "Builder.py"

# 12/18/24 Version 0.3

- Added "Face" class
- Added "utils.py"
- Reworked "Builder" Class
- Added functionality to build second layer of statue

# 12/19/24 Version 0.4

- Added "ImageParser" class
    - Responsible for processing an image file
- Added "dict.py"
- Updated "utils.py"
    - Added "ProcessTextures" function
    - Added "GetDifference" function
    - Added "GetBlock" function
    - Added "ConvertToBlocks" function
- Added docstrings to all current functions and classes

# 12/20/24 Version 1.0

- Added functionality to read first layer of skin and build schematic
- Updated "Face" Class
    - Added Rotation and Reflection functionality
- Updated "utils.py"
    - Added "ReadSkinRegion" function
- Fixed Bug in "Builder" Class
    - 0 Padding caused indexing error in "BuildFace" and "BuildMaskFace" functions

# 2/1/24 Version 1.1

- Added functionality for Slim models
- Updated "main.py"
    - Handles Slim variations for building

# 2/2/24 Version 1.2
- Added functionality to read second kayer of skin and build schematic
    - Added "Second_Layer" variable in "main.py" to toggle mask building
- Updated "ImageParser" Class
    - Now reads image segments as RGBA, to account for transparancy
- Updated "Builder" Class
    - Reworked Mask minimum and maximum values for building and reading