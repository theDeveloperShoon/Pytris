class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.displayGrid = self.grid

    def update(self):
        self.displayGrid = self.grid

    def save(self):
        self.grid = self.displayGrid
        print(self.grid)
