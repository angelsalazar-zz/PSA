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
TAP = 'TAP_CELL_ROW_COL'

from board import toggleCell

class CleanUpPuzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        
    def actions(self, state):
        return [('TAP', (1, 1))]

    def result(self, state, action):
        return toggleCell(state, action[1])

