import unittest

import test_utils

import hate_a


class TestHateA(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            aaaaa
            """,
            """
            aaaaa
            """,
            solve_func=hate_a.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            aacaababc
            """,
            """
            :(
            """,
            solve_func=hate_a.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            ababacacbbcc
            """,
            """
            ababacac
            """,
            solve_func=hate_a.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            baba
            """,
            """
            :(
            """,
            solve_func=hate_a.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            bcbac
            """,
            """
            :(
            """,
            solve_func=hate_a.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
