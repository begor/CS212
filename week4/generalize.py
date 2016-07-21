from cannibals import csuccessors


def mc_problem2(start=(3, 3, 1, 0, 0, 0), goal=None):
    return shortest_path_search(start, csuccessors,
    	lambda state: state == (goal or (0, 0, 0) + start[:3]))


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    # your code here
    Fail = []

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
    return 'tests pass'

print(test())
