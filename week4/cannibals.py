# -----------------
# User Instructions
#
# Write a function, csuccessors, that takes a state (as defined below)
# as input and returns a dictionary of {state:action} pairs.
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings:
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.
#
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.


def csuccessors(state):

    def add(X, Y):
        return tuple(x + y for x, y in zip(X, Y))

    def sub(X, Y):
        return tuple(x - y for x, y in zip(X, Y))

    DELTAS = {(2, 0, 1, -2, 0, -1): 'MM',
              (0, 2, 1, 0, -2, -1): 'CC',
              (1, 1, 1, -1, -1, -1): 'MC',
              (1, 0, 1, -1, 0, -1): 'M',
              (0, 1, 1, 0, -1, -1): 'C'}

    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}

    items = []
    if B1 > 0:
        items += [(sub(state, delta), action + '->')
                  for delta, action in DELTAS.items()]
    if B2 > 0:
        items += [(add(state, delta), '<-' + action)
                  for delta, action in DELTAS.items()]

    return dict(items)


def csuccessors_mine(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""

    M1, C1, B1, M2, C2, B2 = state
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}

    if B1 > 0:
        return {((M1 - m), (C1 - c), B1 - 1, M2 + m, C2 + c, B2 + 1): 'M' * m + 'C' * c + '->'
                for m in range(M1 + 1)
                for c in range(C1 + 1) if 0 < m + c < 3}

    if B2 > 0:
        return {(M1 + m, C1 + c, B1 + 1, M2 - m, C2 - c, B2 - 1): '<-' + 'M' * m + 'C' * c
                for m in range(M2 + 1)
                for c in range(C2 + 1) if 0 < m + c < 3}


def mc_problem(start=(3, 3, 1, 0, 0, 0), goal=None):
    if not goal:
        goal = (0, 0, 0) + start[:3]

    if start == goal:
        return [goal]

    explored = set()
    frontier = [[start]]

    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for state, action in csuccessors_mine(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)


def test(func):
    assert func((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                        (1, 2, 0, 1, 0, 1): 'M->',
                                        (0, 2, 0, 2, 0, 1): 'MM->',
                                        (1, 1, 0, 1, 1, 1): 'MC->',
                                        (2, 0, 0, 0, 2, 1): 'CC->'}
    assert func((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                        (2, 1, 1, 3, 3, 0): '<-M',
                                        (3, 1, 1, 2, 3, 0): '<-MM',
                                        (1, 3, 1, 4, 1, 0): '<-CC',
                                        (2, 2, 1, 3, 2, 0): '<-MC'}
    assert func((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print(test(csuccessors_mine))
print(test(csuccessors))
