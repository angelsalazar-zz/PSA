from board import buildGrid
from board import toggleCell
from board import displayBoard
from cleanUpPuzzle import CleanUpPuzzle


SIZE = 5
puzzle = CleanUpPuzzle(
    buildGrid(size = SIZE), 
    buildGrid(size = SIZE, cellContent = False)
)