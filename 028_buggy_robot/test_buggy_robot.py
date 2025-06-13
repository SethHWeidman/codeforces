import unittest

import test_utils

import buggy_robot


class TestDisplayTheNumber(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            4
            LDUR
            """,
            """
            4
            """,
            solve_func=buggy_robot.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            5
            RRRUU
            """,
            """
            0
            """,
            solve_func=buggy_robot.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            6
            LLRRRR
            """,
            """
            4
            """,
            solve_func=buggy_robot.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
