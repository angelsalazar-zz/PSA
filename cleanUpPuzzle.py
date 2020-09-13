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
TOGGLE = 'TOGGLE'

class CleanUpPuzzle(Problem):

    def __init__(self, initial=(), goal=(0,0,0)):
        Problem.__init__(self, initial, goal)
        self.all_actions = [TOGGLE] # possible actions
        
    def actions(self, state):
        return self.all_actions

        

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError
