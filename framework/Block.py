class Block:
    def __init__(self, xOffset, yOffset):
        self.shape = [[True]]
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.isFalling = True

    def paste_on_grid(self, grid):
        numOfRows = len(self.shape)
        numOfTiles = len(self.shape[0])

        y = 0
        while y < numOfRows:
            x = 0
            while x < numOfTiles:
                if(self.shape[y][x] is True):
                    grid[y+self.yOffset][x+self.xOffset][2] = self.shape[y][x]
                x += 1
            y += 1

        return grid

    def canMoveLeft(self, grid):
        listOfLeftTiles = self.getLeftSide()
        cantMoveLeft = False

        for tile in listOfLeftTiles:
            x = tile[0]
            y = tile[1]
            try:
                if self.xOffset > 0:
                    if grid[y + self.yOffset][self.xOffset + x - 1][2] is True:
                        cantMoveLeft = True
                        break
                else:
                    cantMoveLeft = True
                    break
            except IndexError:
                cantMoveLeft = True
                break
        return not cantMoveLeft

    def getLeftSide(self):
        """
            Creates a row based check for the left side
            Starts on the right side however
        """
        tileNumVert = len(self.shape)
        tileNumHoriz = len(self.shape[0])

        listOfLeftTiles = []

        y = 0
        while y < tileNumVert:
            x = tileNumHoriz - 1
            res = tileNumHoriz - 1
            while x >= 0:
                if self.shape[y][x] is True:
                    res = x
                x -= 1

            myTile = [res, y]
            listOfLeftTiles.append(myTile)
            y += 1

        return listOfLeftTiles

    def canMoveRight(self, grid):
        listOfRightTiles = self.getRightSide()
        cantMoveRight = False

        for tile in listOfRightTiles:
            x = tile[0]
            y = tile[1]
            try:
                if grid[y + self.yOffset][self.xOffset + x + 1][2] is True:
                    cantMoveRight = True
                    break
            except IndexError:
                cantMoveRight = True
                break
        return not cantMoveRight

    def getRightSide(self):
        """
            Creates a row based check for the right side
        """
        tileNumVert = len(self.shape)
        tileNumHoriz = len(self.shape[0])

        listOfRightTiles = []

        y = 0
        while y < tileNumVert:
            x = 0
            res = 0
            while x < tileNumHoriz:
                if self.shape[y][x] is True:
                    res = x
                x += 1
            myTile = [res, y]
            listOfRightTiles.append(myTile)
            y += 1

        return listOfRightTiles

    def canMoveDown(self, grid):
        listOfBottomTiles = self.getBottomSide()
        # print(listOfBottomTiles)
        cantMoveDown = False
        for tile in listOfBottomTiles:
            # print(tile)
            x = tile[0]
            y = tile[1]
            try:
                if grid[y + self.yOffset + 1][self.xOffset + x][2] is True:
                    cantMoveDown = True
                    break
            except IndexError:
                cantMoveDown = True
                break
        return not cantMoveDown

    def getBottomSide(self):
        """
            Want to create a column based check to see the bottom tile
        """
        tileNumVert = len(self.shape)
        tileNumHoriz = len(self.shape[0])

        listOfBottomTiles = []

        x = 0
        while x < tileNumHoriz:
            y = 0
            res = 0
            while y < tileNumVert:
                if self.shape[y][x] is True:
                    res = y
                y += 1

            myTile = [x, res]
            listOfBottomTiles.append(myTile)
            x += 1

        #print(listOfBottomTiles)
        return listOfBottomTiles

    def rotate(self):
        """
            Is similar to getBottomSide where it creates a column based version
            of the grid

            Is not going to be used in product as there has to be a system in
            place to see if it can rotate or not.  But am going to implement it
            just for funs?
        """
        tileNumVert = len(self.shape)
        tileNumHoriz = len(self.shape[0])

        newShape = []
        x = 0
        while x < tileNumHoriz:
            y = tileNumVert - 1
            newRow = []
            while y >= 0:
                newRow.append(self.shape[y][x])
                y -= 1
            newShape.append(newRow)
            x += 1

        return newShape

    def rotateCheck(self, grid):
        """
            Exact same rotate code
        """
        tileNumVert = len(self.shape)
        tileNumHoriz = len(self.shape[0])

        newShape = []
        x = 0
        while x < tileNumHoriz:
            y = tileNumVert - 1
            newRow = []
            while y >= 0:
                newRow.append(self.shape[y][x])
                y -= 1
            newShape.append(newRow)
            x += 1

        # Rotate Check
        canRotate = True

        height = len(newShape)
        width = len(newShape[0])

        try:
            y = 0
            while y < height:
                x = 0
                while x < width:
                    if(grid[y + self.yOffset][x + self.xOffset][2] == True):
                        canRotate = False
                    x += 1
                y += 1
        except IndexError:
            canRotate = False

        if canRotate:
            self.shape = newShape

    def instantDown(self, grid):
        while self.canMoveDown(grid):
            self.yOffset += 1

        self.isFalling = False

    def can_spawn(self, grid):

        tiles = self.get_tiles_relative_to_grid()

        canSpawn = True
        for tile in tiles:
            if grid[tile[1]][tile[0]][2] is True:
                canSpawn = False
                break

        return canSpawn

    def get_tiles_relative_to_grid(self):

        tile_list = []

        height = len(self.shape)
        width = len(self.shape[0])

        y = 0
        while y < height:
            x = 0
            while x < width:
                if self.shape[y][x] is True:
                    tile_list.append([self.xOffset+x, self.yOffset+y])

                x += 1
            y += 1

        return tile_list
