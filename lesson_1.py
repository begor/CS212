def poker(hands):
    """Return the best hand"""
    return max(hands, key=hand_rank)


def hand_rank(hand):
    pass


def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split()  # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    return 'tests passed'


print(test())
