import unittest

import test_utils

import cubes_sorting


class TestCubesSorting(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            3
            5
            5 3 2 1 4
            6
            2 2 2 2 2 2
            2
            2 1
            """,
            """
            YES
            YES
            NO
            """,
            solve_func=cubes_sorting.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
