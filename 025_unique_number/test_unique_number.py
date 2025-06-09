import unittest

import test_utils

import unique_number


class TestUniqueNumber(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            4
            1
            5
            15
            50        
            """,
            """
            1
            5
            69
            -1
            """,
            solve_func=unique_number.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
