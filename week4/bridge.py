def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    if 'light' in here:
        people_h = here - {'light'}
        people_t = frozenset().union(there, {'light'})
        return {(frozenset(people_h - {p}), frozenset().union({p}, people_t), t + p): (p, p, '->')
                for p in people_h}
    else:
        people_t = there - {'light'}
        people_h = frozenset().union(here, {'light'})
        return {(frozenset().union({p}, people_h), frozenset(people_t - {p}), t + p): (p, p, '<-')
                for p in people_t}

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) =={
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()