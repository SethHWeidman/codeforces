import unittest
import make_product_equal_one
import test_utils


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        # Example: n=2, -1 1 -> output 2
        test_utils.test_input_output(
            """
            2
            -1 1
            """,
            "2",
            solve_func=make_product_equal_one.solve,
            test_case=self,
        )

    def test_example_2(self):
        # Example: n=4, 0 0 0 0 -> output 4
        test_utils.test_input_output(
            """
            4
            0 0 0 0
            """,
            "4",
            solve_func=make_product_equal_one.solve,
            test_case=self,
        )

    def test_example_3(self):
        # Example: n=5, -5 -3 5 3 0 -> output 13
        test_utils.test_input_output(
            """
            5
            -5 -3 5 3 0
            """,
            "13",
            solve_func=make_product_equal_one.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
