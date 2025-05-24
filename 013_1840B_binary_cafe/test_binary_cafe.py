import unittest

import test_utils

import binary_cafe


class TestBinaryCafe(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            5
            1 2
            2 1
            2 2
            10 2
            179 100
            """,
            """
            2
            2
            3
            4
            180
            """,
            solve_func=binary_cafe.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
