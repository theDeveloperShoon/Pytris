def create_grid(screen_width,
                screen_height,
                tile_size=16,
                horiz_padding=0,
                vert_padding=0):
    myGrid = []
    for y in range(0+vert_padding, screen_height-(vert_padding*2), tile_size):
        currentRow = []
        for x in range(0+horiz_padding, screen_width-horiz_padding, tile_size):
            gridItem = [x, y, False]
            currentRow.append(gridItem)
        myGrid.append(currentRow)
    return myGrid


class Grid:
    def __init__(self,
                 tile_size,
                 screen_width,
                 screen_height,
                 vert_padding=0,
                 horiz_padding=0):
        self.grid = create_grid(screen_width,
                                screen_height,
                                tile_size,
                                horiz_padding,
                                vert_padding)
        self.displayGrid = create_grid(screen_width,
                                       screen_height,
                                       tile_size,
                                       horiz_padding,
                                       vert_padding)

        self.amountOfClearsinLastProcedure = 0

    def update(self):
        self.clear_display_grid()
        self.paste_grid_on_display_grid()
        # print(self.grid)

    def save(self):
        self.save_display_grid_on_grid()
        # print(self.grid)

    def clear_display_grid(self):
        blankedGrid = []
        for row in self.displayGrid:
            clearedRow = []
            for tile in row:
                newTile = tile
                newTile[2] = False
                clearedRow.append(newTile)
            blankedGrid.append(clearedRow)
        self.displayGrid = blankedGrid

    def clear_data_grid(self):
        numOfRows = len(self.grid)
        numOfTiles = len(self.grid[0])

        y = 0
        while y < numOfRows:
            x = 0
            while x < numOfTiles:
                self.grid[y][x][2] = False
                x += 1
            y += 1

    def reset(self):
        self.clear_data_grid()
        self.clear_display_grid()

    def paste_grid_on_display_grid(self):
        numOfRows = len(self.grid)
        numOfTiles = len(self.grid[0])

        y = 0
        while y < numOfRows:
            x = 0
            while x < numOfTiles:
                self.displayGrid[y][x][2] = self.grid[y][x][2]
                x += 1
            y += 1

    def save_display_grid_on_grid(self):
        numOfRows = len(self.grid)
        numOfTiles = len(self.grid[0])

        y = 0
        while y < numOfRows:
            x = 0
            while x < numOfTiles:
                self.grid[y][x][2] = self.displayGrid[y][x][2]
                x += 1
            y += 1

    def fall_procedure(self):
        self.save()

        clearedRows = self.check_for_clears()
        clearedRows.sort()

        for row in clearedRows:
            self.clear_grid_row(row)
            self.shift_from_above(row)

        self.amountOfClearsinLastProcedure = len(clearedRows)

    def check_for_clears(self):
        listOfIndexesForClearedRows = []

        y = 0
        for row in self.grid:
            rowIsCleared = True
            for tile in row:
                if tile[2] is False:
                    rowIsCleared = False
                    break
            if rowIsCleared:
                listOfIndexesForClearedRows.append(y)
            y += 1

        return listOfIndexesForClearedRows

    def shift_from_above(self, cap):
        """
            Is going to through each row from top to bottom and copying the
            data the row above down.

            Reason why clearedRows in fall_procedure() needs to be sorted
        """
        numOfRows = len(self.grid)
        numOfTiles = len(self.grid[0])

        revisedGrid = []
        for row in self.grid:
            blankRow = []
            for tile in row:
                newTile = tile.copy()
                newTile[2] = False
                blankRow.append(newTile)
            revisedGrid.append(blankRow)

        y = 0
        while y <= cap:
            x = 0
            while x < numOfTiles:
                if y == 0:
                    revisedGrid[y][x][2] = False
                else:
                    revisedGrid[y][x][2] = self.grid[y-1][x][2]
                x += 1
            y += 1

        if (cap != (numOfRows - 1)):
            y = cap + 1
            while y < numOfRows:
                x = 0
                while x < numOfTiles:
                    revisedGrid[y][x][2] = self.grid[y][x][2]
                    x += 1
                y += 1

        self.grid = revisedGrid

    def clear_grid_row(self, index):
        row = self.grid[index]

        for tile in row:
            tile[2] = False
