def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    # your code here
    here, there = state
    l = 'light'
    if l in here:
        return {(here - frozenset([a, b, l]),
                 there | frozenset([a, b, l])): (a, b, '->')
                for a in here if a is not l
                for b in here if b is not l}
    else:
        return {(here | frozenset([a, b, l]),
                 there - frozenset([a, b, l])): (a, b, '<-')
                for a in there if a is not l
                for b in there if b is not l}


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    l = 'light'
    if l in here:
        return {(here - frozenset([a, b, l]),
                 there | frozenset([a, b, l]),
                 t + max(a, b)): (a, b, '->')
                for a in here if a is not l
                for b in here if b is not l}
    else:
        return {(here | frozenset([a, b, l]),
                 there - frozenset([a, b, l]),
                 t + max(a, b)): (a, b, '<-')
                for a in there if a is not l
                for b in there if b is not l}


def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = (state, (action, total_cost), state, ... )
    if len(path) < 3:
        return 0
    else:
        return path[-2][1]


def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem.
    An action is an (a, b, arrow) tuple; a and b are
    times; arrow is a string.
    """
    a, b, arrow = action
    return max(a, b)


def path_states(path):
    "Return a list of states in this path."
    return path[::2]


def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


def elapsed_time(path):
    return path[-1][2]


def bridge_problem(here):
    """Modify this to test for goal later: after pulling a state off frontier,
    not when we are about to put it on the frontier."""
    # modify code below
    here = frozenset(here) | frozenset(['light'])
    explored = set()  # set of states we have visited
    # State will be a (people-here, people-there, time-elapsed)
    # ordered list of paths we have blazed
    frontier = [[(here, frozenset(), 0)]]
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        here = path[-1][0]
        if not here:
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return []


def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5),  # state 1
                # action 1
                (5, 2, '->'),
                (frozenset([10, 5]), frozenset(
                    [1, 2, 'light']), 2),  # state 2
                # action 2
                (2, 1, '->'),
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (5, 5, '->'),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (5, 10, '->'),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (2, 2, '->'),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (10, 1, '->'),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (10, 10, '->'),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (10, 2, '->'),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (5, 1, '->'),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                (1, 1, '->')]
    assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5),  # state 1
                                     (frozenset([10, 5]), frozenset(
                                         [1, 2, 'light']), 2),  # state 2
                                     (frozenset([1, 2, 10]),
                                      frozenset(['light', 5]), 5),
                                     (frozenset([1, 2]), frozenset(
                                         ['light', 10, 5]), 10),
                                     (frozenset([1, 10, 5]),
                                      frozenset(['light', 2]), 2),
                                     (frozenset([2, 5]), frozenset(
                                         [1, 10, 'light']), 10),
                                     (frozenset([1, 2, 5]),
                                      frozenset(['light', 10]), 10),
                                     (frozenset([1, 5]), frozenset(
                                         ['light', 2, 10]), 10),
                                     (frozenset([2, 10]), frozenset(
                                         [1, 5, 'light']), 5),
                                     (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
    assert path_actions(testpath) == [(5, 2, '->'),  # action 1
                                      (2, 1, '->'),  # action 2
                                      (5, 5, '->'),
                                      (5, 10, '->'),
                                      (2, 2, '->'),
                                      (10, 1, '->'),
                                      (10, 10, '->'),
                                      (10, 2, '->'),
                                      (5, 1, '->'),
                                      (1, 1, '->')]

    # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2),))[-1][-1] == 2
    assert bridge_problem(frozenset((1, 2, 5, 10),))[-1][-1] == 17

    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bsuccessors2((here1, there1)) == {
        (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
        (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'),
        (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'),
        (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}

    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2',
                      ((3, 4, '<-'), 6), 'fs3')) == 6
    assert bcost((4, 2, '->'),) == 4
    assert bcost((3, 10, '<-'),) == 10
    return 'tests pass'


print(test())
