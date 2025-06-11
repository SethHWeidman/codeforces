import unittest

import test_utils

import make_it_increasing


class TestMakeItIncreasing(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            7
            3
            3 6 5
            5
            1 2 3 4 5
            1
            1000000000
            4
            2 8 7 5
            5
            8 26 5 21 10
            2
            5 14
            3
            4 0 5
            """,
            """
            2
            0
            0
            4
            11
            0
            -1
            """,
            solve_func=make_it_increasing.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
