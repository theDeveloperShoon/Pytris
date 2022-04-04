class Block:
    def __init__(self, myGrid, xOffset, yOffset):
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
