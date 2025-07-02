import unittest

import test_utils

import case_of_fake_numbers


class TestCaseOfFakeNumbers(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            3
            1 0 0
            """,
            """
            Yes
            """,
            solve_func=case_of_fake_numbers.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            5
            4 2 1 4 3
            """,
            """
            Yes
            """,
            solve_func=case_of_fake_numbers.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            4
            0 2 3 1
            """,
            """
            No
            """,
            solve_func=case_of_fake_numbers.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
