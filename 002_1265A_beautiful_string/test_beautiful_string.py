import unittest
import test_utils

import beautiful_string


class TestBeautifulString(unittest.TestCase):
    def test_sample_cases(self):
        test_utils.test_input_output(
            """
            3
            a???cb
            a??bbc
            a?b?c
            """,
            """
            ababcb
            -1
            acbac
            """,
            solve_func=beautiful_string.solve,
            test_case=self,
        )

    def test_additional_cases(self):
        test_utils.test_input_output(
            """
            5
            ?
            ??
            a?
            ?b
            abc?
            """,
            """
            a
            ab
            ab
            ab
            abca
            """,
            solve_func=beautiful_string.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
