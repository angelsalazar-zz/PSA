import random

random.randint(0, 1)

def buildGrid(size, cellContent = None):
    rows = list()
    for _ in range(size):
        cols = list()
        for _ in range(size):
            if (cellContent):
                cols.append(cellContent)
            else:
                cols.append(random.randint(0, 1) == 1)
        rows.append(cols)
    return rows

class Board:
    def __init__(self, size = 5, grid = None):
        self.SIZE = size
        if grid:
            self.grid = grid
        else:
            self.grid = buildGrid(size)

    def toggleCell(self, position):
        row, col = position
        # affected cells (Order matters)
        cells = [
                            (row - 1, col),     
            (row, col - 1),                 (row, col + 1),
                            (row + 1, col)    
        ]

        for cell in cells:
            if (
                cell[0] < 0 or 
                cell[0] > 4 or
                cell[1] < 0 or
                cell[1] > 4
            ):
                continue
            print(cell)
            self.grid[cell[0]][cell[1]] = not self.grid[cell[0]][cell[1]]

    def getState(self):
        rows = []
        for row in self.grid:
            rows.append(row.copy())
        return rows

    def toString(self):
        rows = []
        for row in self.grid:
            r = []
            for cell in row:
                r.append('    {0!s:8}'.format(cell))
            rows.append('|'.join(r))
        return '\n'.join(rows)

    def display(self):
        print(self.toString())
            



