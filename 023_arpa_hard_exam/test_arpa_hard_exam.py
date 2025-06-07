import unittest

import test_utils

import arpa_hard_exam


class TestArpaHardExam(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            1        
            """,
            """
            8
            """,
            solve_func=arpa_hard_exam.solve,
            test_case=self,
        )

    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2       
            """,
            """
            4
            """,
            solve_func=arpa_hard_exam.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
