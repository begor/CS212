"""CS212 Homework1-1."""
import itertools
from poker import hand_rank


def best_hand(hand):
    """Take a seven card hand as input and returns the best possible 5."""
    return max(itertools.combinations(hand, 5), key=hand_rank)


def best_wild_hand(hand):
    """
    Return best hand based on given wild hand.

    Takes a hand which may contain Jokers, and return highest ranked
    hand with Jokers replaced.
    """
    def replacements(card):
        """Replace given card (if it's Joker) with possible cards."""
        allranks = '23456789TJQKA'
        b_cards = [r + s for r in allranks for s in 'SC']
        r_cards = [r + s for r in allranks for s in 'HD']

        if card == '?B':
            return b_cards
        if card == '?R':
            return r_cards
        else:
            return [card]  # we should always return a list

    replaced_hands = map(replacements, hand)
    variants = (best_hand(h) for h in itertools.product(*replaced_hands))
    return max(variants, key=hand_rank)
