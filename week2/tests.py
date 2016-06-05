import unittest
from problem_set import faster_solve, floor_puzzle, longest_subpalindrome_slice


class ProblemSetTests(unittest.TestCase):

    def test_simple_faster_solve(self):
        """Easy test."""
        self.assertEqual(faster_solve('X / X == X'), '1 / 1 == 1')

    def test_faster_solve_with_many_answers(self):
        """Faster solve should return one of the possible answers."""
        self.assertIn(
            faster_solve('YOU == ME**2'),
            ('289 == 17**2', '576 == 24**2', '841 == 29**2', '324 == 18**2'))

    def test_faster_solve_with_leading_zero(self):
        """Faster solve should NOT return '1 + 0 == 01'."""
        self.assertIsNone(faster_solve('A + B == BA'))

    def test_floor_puzzle(self):
        """Floor puzzle should return correct list of floors."""
        self.assertEqual(floor_puzzle(), [1, 2, 3, 5, 4])

    def test_longest_subpalindrome(self):
        """Longest subpalindrome of a palindrome text is itself text."""
        self.assertEqual(longest_subpalindrome_slice('racecar'), (0, 7))

    def test_longest_subpalindrome_with_capital(self):
        """Longest subpalindrome of a palindrome text is itself text."""
        self.assertEqual(longest_subpalindrome_slice('RaCecar'), (0, 7))

    def test_longest_subpalindrome_of_non_palindrome(self):
        """It should return longest subpalindrome from a non palindrome text."""
        self.assertEqual(longest_subpalindrome_slice('RaCecarX'), (0, 7))


    def test_longest_subpalindrome_of_empty_text_is_beginning(self):
        """Given empty string longest_subpalindrome_slice should return 0, 0."""
        self.assertEqual(longest_subpalindrome_slice(''), (0, 0))

    def test_longest_subpalindrome_with_spaces(self):
        """Procedure should correctly handle strings w/ spaces."""
        self.assertEqual(longest_subpalindrome_slice('Mad am I ma dam.'), (0, 15))


if __name__ == '__main__':
    unittest.main()
