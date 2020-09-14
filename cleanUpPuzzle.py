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
FIND_DIAMOND = 'FIND_DIAMOND'
FIND_DIAMOND_IN_EDGE = 'FIND_DIAMOND_IN_EDGE'
CLEAN = 'CLEAN'

class CleanUpPuzzle(Problem):
    def __init__(self, initial, goal):
        Problem.__init__(self, initial, goal)
        self.all_actions = [FIND_DIAMOND, FIND_DIAMOND_IN_EDGE, CLEAN]
        
    def actions(self, state):
        actions = []
        
        # for action in self.all_actions:

        #     if action == 'M1M' and \
        #        not illegal_state(new_state(state,1,0), self.misycan):
        #         actions.append('M1M')
        #     elif action == 'M2M' and \
        #          not illegal_state(new_state(state,2,0), self.misycan):
        #         actions.append('M2M')
        #     elif action == 'M1C' and \
        #          not illegal_state(new_state(state,0,1), self.misycan):
        #         actions.append('M1C')
        #     elif action == 'M2C' and \
        #          not illegal_state(new_state(state,0,2), self.misycan):
        #         actions.append('M2C')
        #     elif action == 'M1M1C' and \
        #          not illegal_state(new_state(state,1,1), self.misycan):
        #         actions.append('M1M1C')        
        return actions


# def new_state(state, mis, can):
#     """Moves mis missionaries and can cannibals to get a new state.
#     The resulting state is not verified (may be invalid)"""
#     nstate = list(state)
#     if nstate[2] == 0:
#         nstate[2] = 1
#     else:
#         mis = - mis
#         can = - can
#         nstate[2] = 0
#     nstate[0] = nstate[0] + mis
#     nstate[1] = nstate[1] + can
#     return tuple(nstate)
    

        # return self.all_actions

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError
