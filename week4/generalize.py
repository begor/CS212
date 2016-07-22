from cannibals import csuccessors
from bridge import add_to_frontier, path_cost, bsuccessors2, bcost, final_state


Fail = []


def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    return shortest_path_search(start, csuccessors,
                                lambda state: state == (goal or (0, 0, 0) + start[:3]))


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    # your code here

    if is_goal(start):
        return [start]

    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        state = path[-1]
        for (state, action) in successors(state).items():
            if state not in explored:
                explored.add(state)
                new_path = path + [action, state]
                if is_goal(state):
                    return new_path
                else:
                    frontier.append(new_path)
    return Fail


def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    if is_goal(start):
        return [start]

    explored = set()
    frontier = [ [start] ]
    while frontier:
        path = frontier.pop(0)
        state1 = final_state(path)
        if is_goal(state1):  
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail




def bridge_problem3(here):
    """Find the fastest (least elapsed time) path to 
    the goal in the bridge problem."""
    # your code here
    def is_goal(state):
        here, there = state
        return not here or here == set(['light'])

    start = (frozenset(here) | frozenset(['light']), frozenset())
    return lowest_cost_search(start, bsuccessors2, is_goal, bcost)


def test():

    def is_goal(state):
        if state == 8:
            return True
        else:
            return False

    def successors(state):
        successors = {state + 1: '->',
                      state - 1: '<-'}
        return successors

    assert shortest_path_search(5, successors, is_goal) == [
        5, '->', 6, '->', 7, '->', 8]

    assert mc_problem2(start=(1, 1, 1, 0, 0, 0)) == [
        (1, 1, 1, 0, 0, 0), 'MC->',
        (0, 0, 0, 1, 1, 1)]
    assert mc_problem2() == [(3, 3, 1, 0, 0, 0), 'CC->',
                             (3, 1, 0, 0, 2, 1), '<-C',
                             (3, 2, 1, 0, 1, 0), 'CC->',
                             (3, 0, 0, 0, 3, 1), '<-C',
                             (3, 1, 1, 0, 2, 0), 'MM->',
                             (1, 1, 0, 2, 2, 1), '<-MC',
                             (2, 2, 1, 1, 1, 0), 'MM->',
                             (0, 2, 0, 3, 1, 1), '<-C',
                             (0, 3, 1, 3, 0, 0), 'CC->',
                             (0, 1, 0, 3, 2, 1), '<-C',
                             (0, 2, 1, 3, 1, 0), 'CC->',
                             (0, 0, 0, 3, 3, 1)]
    here = [1, 2, 5, 10]
    assert bridge_problem3(here) == [
            (frozenset([1, 2, 'light', 10, 5]), frozenset([])), 
            ((2, 1, '->'), 2), 
            (frozenset([10, 5]), frozenset([1, 2, 'light'])), 
            ((2, 2, '<-'), 4), 
            (frozenset(['light', 10, 2, 5]), frozenset([1])), 
            ((5, 10, '->'), 14), 
            (frozenset([2]), frozenset([1, 10, 5, 'light'])), 
            ((1, 1, '<-'), 15), 
            (frozenset([1, 2, 'light']), frozenset([10, 5])), 
            ((2, 1, '->'), 17), 
            (frozenset([]), frozenset([1, 10, 2, 5, 'light']))]
    return 'test passes'

print(test())
