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
    """Return tuple indicating a value of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    # Check if cards forms ace low straight
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """Return True if all the cards have the same suit."""
    suites = [s for r, s in hand]
    return len(set(suites)) == 1


def kind(n, ranks):
    """
    Find rank that appears n times in ranks.

    Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand.
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r


def two_pair(ranks):
    """
    Assume if there are two pairs in ranks.

    If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None.
    """
    pair = kind(2, ranks)
    lower_pair = kind(2, list(reversed(ranks)))
    if pair and lower_pair != pair:
        return pair, lower_pair


def test():
    """Test cases for the functions in poker program."""
    sf1 = "6C 7C 8C 9C TC".split()
    sf2 = "6D 7D 8D 9D TD".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    tp = "TD 9H TH 9C 3S".split()
    al = "AC 2D 4H 3D 5S".split()
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert straight(card_ranks(al))
    assert card_ranks(sf1) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]
    assert poker([sf1, fk, fh]) == [sf1]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker(100 * [fh]) == 100 * [fh]
    assert hand_rank(sf1) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) is None
    assert kind(2, fkranks) is None
    assert kind(1, fkranks) == 7
    assert two_pair(tpranks) == (10, 9)
    return 'tests passed'

print(test())
