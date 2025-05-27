import unittest

import test_utils

import parliament_of_berland


class TestTheTime(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            3 2 2
            """,
            """
            1 2
            0 3
            """,
            solve_func=parliament_of_berland.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            8 4 3
            """,
            """
            1 2 3
            4 5 6
            7 8 0
            0 0 0
            """,
            solve_func=parliament_of_berland.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            10 2 2
            """,
            """
            -1
            """,
            solve_func=parliament_of_berland.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
