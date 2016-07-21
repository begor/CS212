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


def is_goal(state):
    if state == 8:
        return True
    else:
        return False


def successors(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors

# test
assert shortest_path_search(5, successors, is_goal) == [
    5, '->', 6, '->', 7, '->', 8]
