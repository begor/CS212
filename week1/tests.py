import unittest
from poker import poker
from problem_set import best_hand


class LessonTests(unittest.TestCase):
    """Test suite for Lesson and Problem Set on Week 1."""

    def setUp(self):
        """Test data: common poker hands."""
        self.sf1 = "6C 7C 8C 9C TC".split()
        self.sf2 = "6D 7D 8D 9D TD".split()
        self.fk = "9D 9H 9S 9C 7D".split()
        self.fh = "TD TC TH 7C 7D".split()
        self.tp = "TD 9H TH 9C 3S".split()
        self.al = "AC 2D 4H 3D 5S".split()

    def test_poker_one_sf(self):
        """In a regular poker hands, winner should be SF."""
        self.assertEqual(poker([self.sf1, self.fk, self.fh]), [self.sf1])

    def test_poker_two_sf(self):
        """If there are two SFs, they both should be in result."""
        self.assertEqual(
            poker([self.sf1, self.sf2, self.fk, self.fh]),
            [self.sf1, self.sf2])

    def test_four_kind(self):
        """FK is better then FH."""
        self.assertEqual(poker([self.fk, self.fh]), [self.fk])

    def test_two_full_house(self):
        """If there are two FHs, they both should be in result."""
        self.assertEqual(poker([self.fh, self.fh]), [self.fh, self.fh])

    def test_more_values(self):
        """Poker function should work fine no matter how big input is."""
        self.assertEqual(poker(100 * [self.fh]), 100 * [self.fh])

    def test_seven_cards_poker(self):
        """Best hand should return 5 best combination out of 7-cards hand."""
        self.assertEqual(best_hand("6C 7C 8C 9C TC 5C JS".split()),
                         ('6C', '7C', '8C', '9C', 'TC'))
        self.assertEqual(best_hand("TD TC TH 7C 7D 8C 8S".split()),
                         ('TD', 'TC', 'TH', '8C', '8S'))
        self.assertEqual(best_hand("JD TC TH 7C 7D 7S 7H".split()),
                         ('JD', '7C', '7D', '7S', '7H'))

if __name__ == '__main__':
    unittest.main()
