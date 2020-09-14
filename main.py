from board import Board
from board import buildGrid
from cleanUpPuzzle import CleanUpPuzzle

SIZE = 5
puzzle = CleanUpPuzzle(
    Board(size = SIZE), 
    Board(grid = buildGrid(size = SIZE, cellContent = False))
)

b = Board(size = SIZE)
b.display()