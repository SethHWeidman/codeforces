import unittest

import test_utils

import initial_bet


class TestInitialBet(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2 5 4 0 4
            """,
            """
            3
            """,
            solve_func=initial_bet.solve,
            test_case=self,
        )

    def test_official_cases(self):
        test_utils.test_input_output(
            """
            4 5 9 2 1
            """,
            """
            -1
            """,
            solve_func=initial_bet.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
