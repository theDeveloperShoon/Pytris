class Block:
    def __init__(self, xOffset, yOffset):
        self.shape = [[True]]
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.isFalling = True

    def paste_on_grid(self, myGrid):
        numOfRows = len(self.shape)
        numOfTiles = len(self.shape[0])

        y = 0
        while y < numOfRows:
            x = 0
            while x < numOfTiles:
                myGrid[y+self.yOffset][x+self.xOffset][2] = self.shape[y][x]
                x += 1
            y += 1

    def canMoveDown(self, grid):
        listOfBottomTiles = self.getBottomSide()
        # print(listOfBottomTiles)
        cantMoveDown = False
        for tile in listOfBottomTiles:
            # print(tile)
            x = tile[0]
            y = tile[1]
            try:
                if grid[y + self.yOffset + 1][self.xOffset + x] is True:
                    cantMoveDown = True
                    break
            except IndexError:
                cantMoveDown = True
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

        # print(listOfBottomTiles)
        return listOfBottomTiles
