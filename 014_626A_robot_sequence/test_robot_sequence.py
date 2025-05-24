import unittest

import test_utils

import robot_sequence


class TestRobotSequence(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            6
            URLLDR
            """,
            """
            2
            """,
            solve_func=robot_sequence.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            4
            DLUU
            """,
            """
            0
            """,
            solve_func=robot_sequence.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            7
            RLRLRLR
            """,
            """
            12
            """,
            solve_func=robot_sequence.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
