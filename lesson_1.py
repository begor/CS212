def poker(hands):
    """Return the best hand"""
    return max(hands, key=hand_rank)


def hand_rank(hand):
    pass
