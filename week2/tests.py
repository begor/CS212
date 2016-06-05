import unittest
from problem_set import faster_solve


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


if __name__ == '__main__':
    unittest.main()
