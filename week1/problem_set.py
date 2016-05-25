"""CS212 Homework1-1."""
import itertools
from poker import hand_rank


def best_hand(hand):
    """Take a seven card hand as input and returns the best possible 5."""
    return max(itertools.permutations(hand, 5), key=hand_rank)
