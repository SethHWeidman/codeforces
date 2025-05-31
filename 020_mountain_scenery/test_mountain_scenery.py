import unittest

import test_utils

import mountain_scenery


class TestMountainScenery(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            3 2
            0 5 3 5 1 5 2
            """,
            """
            0 4 3 4 1 5 2 
            """,
            solve_func=mountain_scenery.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            1 1
            0 2 0
            """,
            """
            0 1 0
            """,
            solve_func=mountain_scenery.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            3 3
            0 100 35 67 40 60 3
            """,
            """
            0 99 35 66 40 59 3 
            """,
            solve_func=mountain_scenery.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
