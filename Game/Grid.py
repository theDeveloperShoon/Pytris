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
