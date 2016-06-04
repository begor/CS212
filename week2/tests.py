import unittest
from problem_set import faster_solve


class ProblemSetTests(unittest.TestCase):

    def test_faster_solve_with_leading_zero(self):
        """Faster solve should NOT return '1 + 0 == 01'"""
        self.assertIsNone(faster_solve('A + B == BA'))


if __name__ == '__main__':
    unittest.main()
