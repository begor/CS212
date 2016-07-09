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


def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
        (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
        (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    return 'tests pass'

print test()
