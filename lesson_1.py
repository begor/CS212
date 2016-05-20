"""Lesson 1. Poker game function."""

import random


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    """Return numhands for n cards each from deck."""
    return [random.sample(deck, n) for i in range(numhands)]


def poker(hands):
    """
    Return a list of winning hands.

    poker([hand,...]) => [hand,...].
    """
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    key = key or (lambda x: x)
    maximum = max(iterable, key=key)
    return [i for i in iterable if key(i) == key(maximum)]


def hand_rank(hand):
    """Return value indicating how high the hand ranks."""
    def unzip(pairs):
        return zip(*pairs)

    rankings = {(5,): 10,
                (4, 1): 7,
                (3, 2): 6,
                (3, 1, 1): 3,
                (2, 2, 1): 2,
                (2, 1, 1, 1): 1,
                (1, 1, 1, 1, 1): 0}

    ranks_in_hand = ['--23456789TJQKA'.index(r) for r, s in hand]
    groups = group(ranks_in_hand)
    counts, ranks = unzip(groups)
    ranks = (5, 4, 3, 2, 1) if ranks == (14, 5, 4, 3, 2) else ranks
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r, s in hand])) == 1
    straight_flush = 4 * straight + 5 * flush
    return max(rankings[counts], straight_flush), ranks


def group(items):
    """Return a list of [(count, x)...], highest count first."""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def test():
    """Test cases for the functions in poker program."""
    sf1 = "6C 7C 8C 9C TC".split()
    sf2 = "6D 7D 8D 9D TD".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "TD 9H TH 9C 3S".split()
    al = "AC 2D 4H 3D 5S".split()
    assert poker([sf1, fk, fh]) == [sf1]
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker(100 * [fh]) == 100 * [fh]
    return 'tests passed'

print(test())
