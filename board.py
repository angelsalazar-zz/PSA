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

def toggleCell(board, position):
    row, col = position
    AFFECTED_CELLS = [
                    (row - 1, col),     
    (row, col - 1),                 (row, col + 1),
                    (row + 1, col)    
    ]
    for cell in AFFECTED_CELLS:
        if (
            cell[0] < 0 or 
            cell[0] > 4 or
            cell[1] < 0 or
            cell[1] > 4
        ):
            continue
        
        board[cell[0]][cell[1]] = not board[cell[0]][cell[1]]

def displayBoard(board):
    rows = []
    for row in board:
        r = []
        for cell in row:
            r.append('    {0!s:8}'.format(cell))
        rows.append('|'.join(r))
    return '\n'.join(rows)
