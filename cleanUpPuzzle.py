# Implement a class to solve the problem of "Missionaries and Cannibals"
# It includes examples of its use to solve it using the Breadth-first
# algorithm
#
# Author: Dr. Santiago Enrique Conant Pablos
# Date: August 24, 2016

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

class CleanUpPuzzle(Problem):

    def __init__(self, initial=(3,3,1), goal=(0,0,0), myc=3):
        Problem.__init__(self, initial, goal)
        self.misycan = myc # No. of missionaries = No. of cannibals
        self.all_actions = ['M1M','M2M','M1C','M2C','M1M1C'] # possible actions
        
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        return []

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError


    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError