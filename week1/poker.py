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


print(test())
