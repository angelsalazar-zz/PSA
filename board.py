import random

def getAffectedCellsByPosition(position, size):
    row, col = position
    allAffectedCells = []
    # allAffectedCells = [
    #                     (row - 1, col),     
    #     (row, col - 1),                 (row, col + 1),
    #                     (row + 1, col)    
    # ]
    # order matters
    if row - 1 >= 0: allAffectedCells.append((row - 1, col))
    if col - 1 >= 0: allAffectedCells.append((row, col - 1))
    if col + 1 < size: allAffectedCells.append((row, col + 1))
    if row + 1 < size: allAffectedCells.append((row + 1, col))

    return allAffectedCells

# if filler is provided
# tiles are meant to have a fix position for testing porpuses
def buildGrid(size = 5, maxTiles = 10, filler = None):
    tileCounter = 0
    rows = list()
    for r in range(size):
        row = list()
        for c in range(size):
            if filler:
                row.append(filler(r, c))
            else:
                strBit = '0'
                if tileCounter < maxTiles:
                    bit = random.randint(0, 1)
                    if (bit > 0):
                        tileCounter += 1
                        strBit = str(bit)
                row.append(strBit)
        rows.append('|'.join(row))
    return '\n'.join(rows)

def toggleCell(board, position):
    rows = board.split('\n')
    affectedCells = getAffectedCellsByPosition(position, len(rows))
    for cell in affectedCells:
        row = rows[cell[0]].split('|')
        row[cell[1]] = '1' if row[cell[1]] == '0' else '0'
        rows[cell[0]] = '|'.join(row)
    return '\n'.join(rows)

def parseBoard(board):
    rows = []
    encodedRows = board.split('\n')
    for encodedRow in encodedRows:
        rows.append(encodedRow.split('|'))
    return rows