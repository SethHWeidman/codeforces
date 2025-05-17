import unittest

import test_utils

import cableway


class TestCableway(unittest.TestCase):
    def test_official_cases(self):
        # sample 1
        test_utils.test_input_output(
            """
            1 3 2
            """,
            """
            34
            """,
            solve_func=cableway.solve,
            test_case=self,
        )
        # sample 2
        test_utils.test_input_output(
            """
            3 2 1
            """,
            """
            33
            """,
            solve_func=cableway.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
