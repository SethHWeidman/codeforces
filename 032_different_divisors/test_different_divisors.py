import unittest

import test_utils

import different_divisors


class TestInitialBet(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2
            1
            2
            """,
            """
            6
            15
            """,
            solve_func=different_divisors.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
