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
    def __init__(self, grid):
        self.grid = grid
        self.displayGrid = grid

    def update(self):
        self.displayGrid = self.grid

    def save(self):
        self.grid = self.displayGrid
        print(self.grid)

    def clear_grid(self):
        blankedGrid = []
        for row in self.displayGrid:
            clearedRow = []
            for tile in row:
                newTile = tile
                newTile[2] = False
                clearedRow.append(newTile)
            blankedGrid.append(clearedRow)
        self.displayGrid = blankedGrid
