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

    def check_for_clears(self):
        print("Placeholder for now")
