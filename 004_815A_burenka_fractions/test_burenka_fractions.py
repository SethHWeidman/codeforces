import unittest

import test_utils

import burenka_fractions


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        test_utils.test_input_output(
            """
            8
            2 1 1 1
            6 3 2 1
            1 2 2 3
            0 1 0 100
            0 1 228 179
            100 3 25 6
            999999999 300000000 666666666 100000000
            33 15 0 84
            """,
            """
            1
            0
            2
            0
            1
            1
            1
            1
            """,
            solve_func=burenka_fractions.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
