import unittest

import test_utils

import what_is_for_dinner


class TestInitialBet(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            4 3 18
            2 3
            1 2
            3 6
            2 3
            """,
            """
            11
            """,
            solve_func=what_is_for_dinner.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            4 3 18
            2 1
            1 2
            3 6
            2 3
            """,
            """
            9
            """,
            solve_func=what_is_for_dinner.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            2 2 13
            1 13
            2 12
            """,
            """
            13
            """,
            solve_func=what_is_for_dinner.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            2 2 7
            1 13
            2 12
            """,
            """
            7
            """,
            solve_func=what_is_for_dinner.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
