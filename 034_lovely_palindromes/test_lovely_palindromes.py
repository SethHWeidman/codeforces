import unittest

import test_utils

import lovely_palindromes


class TestLovelyPalindromes(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            1
            """,
            """
            11
            """,
            solve_func=lovely_palindromes.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            10
            """,
            """
            1001
            """,
            solve_func=lovely_palindromes.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            27
            """,
            """
            2772
            """,
            solve_func=lovely_palindromes.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
