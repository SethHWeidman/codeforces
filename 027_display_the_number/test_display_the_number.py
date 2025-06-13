import unittest

import test_utils

import display_the_number


class TestDisplayTheNumber(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2
            3
            4
            """,
            """
            7
            11
            """,
            solve_func=display_the_number.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
