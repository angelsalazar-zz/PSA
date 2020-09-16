import random

def getAffectedCellsByPosition(position):
    row, col = position
    return (
        [
                        (row - 1, col),     
        (row, col - 1),                 (row, col + 1),
                        (row + 1, col)    
        ]
    )

def buildGrid(size = 5, filler = None):
    rows = list()
    for r in range(size):
        row = list()
        for c in range(size):
            row.append(filler(r, c) if filler else str(random.randint(0, 1)))
        rows.append('|'.join(row))
    return '\n'.join(rows)

def toggleCell(board, position):
    rows = board.split('\n')
    affectedCells = getAffectedCellsByPosition(position)
    for cell in affectedCells:
        if (
            cell[0] < 0 or 
            cell[0] > 4 or
            cell[1] < 0 or
            cell[1] > 4
        ):
            continue
        row = rows[cell[0]].split('|')
        row[cell[1]] = '1' if row[cell[1]] == '0' else '0'
        rows[cell[0]] = '|'.join(row)
    return '\n'.join(rows)
