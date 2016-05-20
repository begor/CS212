"""Lesson 1. Poker game function."""


def poker(hands):
    """Return the best hand."""
    return max(hands, key=hand_rank)


def hand_rank(hand):
    """Return a tuple indicating the ranking of a hand."""


def test():
    """Test cases for the functions in poker program."""
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker(100 * [fh]) == fh
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests passed'


print(test())
