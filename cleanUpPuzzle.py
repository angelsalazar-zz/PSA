from search import ( # Bases for problem building
    Problem, Node, Graph, UndirectedGraph,
    SimpleProblemSolvingAgentProgram,
    GraphProblem
)

from search import ( # Uninformed search algorithms
    tree_search, graph_search, best_first_graph_search,
    breadth_first_tree_search, breadth_first_search,
    depth_first_tree_search, depth_first_graph_search,
    depth_limited_search, iterative_deepening_search,
    uniform_cost_search,
    compare_searchers
)

#### allow actions
TAB = 'TAB'
from board import toggleCell
from board import getAffectedCellsByPosition
from board import parseBoard

class CleanUpPuzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        
    def actions(self, state):
        return getPossibleMovements(state)

    def result(self, state, action):
        return toggleCell(state, action[1])

# getPossibleMovements scans the full board
# which is not optimal (a more efficient algorithm is needed)
def getPossibleMovements(state):
    board = parseBoard(state)
    size = len(board)
    actions = []
    for row in range(size):
        for col in range(size):
            affectedCells = getAffectedCellsByPosition((row, col), size)
            for cell in affectedCells:
                if board[cell[0]][cell[1]] == '1':
                    actions.append((TAB, (row, col)))
                    break
    
    return actions