import unittest

import test_utils

import the_time


class TestTheTime(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            23:59
            10
            """,
            """
            00:09
            """,
            solve_func=the_time.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            20:20
            121
            """,
            """
            22:21
            """,
            solve_func=the_time.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            10:10
            0
            """,
            """
            10:10
            """,
            solve_func=the_time.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
