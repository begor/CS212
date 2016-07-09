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


def path_states(path):
    "Return a list of states in this path."
    return path[::2]


def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


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

    return 'tests pass'

print test()
