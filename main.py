from board import buildGrid
from board import toggleCell
from board import buildGrid
from board import parseBoard
from cleanUpPuzzle import CleanUpPuzzle
from search import breadth_first_search
from search import uniform_cost_search
import time

SIZE = 6
# REALLY easy problem
def filler(row, col):
    if row == 1 and col == 2: return '1'
    if row == 2 and col == 3: return '1'
    if row == 3 and col == 0: return '1'
    if row == 4 and col == 1: return '1'
    if row == 3 and col == 4: return '1'
    if row == 4 and col == 3: return '1'
    
    # cross
    # if row == 0 and col == 1: return '1'
    # if row == 1 and col == 0: return '1'
    # if row == 1 and col == 2: return '1'
    # if row == 2 and col == 1: return '1'

    # # cross
    # if row == 2 and col == 2: return '1'
    # if row == 3 and col == 1: return '1'
    # if row == 3 and col == 3: return '1'
    # if row == 4 and col == 2: return '1'

    # # bottom right corner
    # if row == 4 and col == 3: return '1'
    # if row == 3 and col == 4: return '1'

    return '0'

def solutionFiller(row, col): 
    return '0'

HARD_BOARD = (
    '0|1|0|0|0|1',
    '0|0|1|0|0|0',
    '0|0|0|1|0|1',
    '0|1|0|0|1|0',
    '0|0|1|0|0|0',
    '0|0|0|0|0|0'
)


puzzle = CleanUpPuzzle(
    '\n'.join(HARD_BOARD), 
    buildGrid(size = SIZE, filler = solutionFiller)
)

def display_solution(goal_node):
    actions = goal_node.solution()
    nodes = goal_node.path()
    print('SOLUTION')
    print('State:' )
    print(nodes[0].state)

    for na in range(len(actions)):
        print('ACTION: ' + str(actions[na]))
        print('State:')
        print(nodes[na+1].state)
    print('END')

# Solving the problem 1:
print("Solution of Problem 1 through Breadth-first search")

start_time = time.time()
goal1 = breadth_first_search(puzzle)
print("--- %s seconds ---" % (time.time() - start_time))

if goal1:
    display_solution(goal1)
else:
    print("Failure: no solution found")