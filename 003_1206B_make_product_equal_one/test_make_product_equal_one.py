import unittest
import make_product_equal_one
import test_utils


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        # -1 -> 1 costs 2
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
        # 0 -> 1 4 times costs 4
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
        # -5 -> -1 costs 4
        # -3 -> -1 costs 2
        # 5 -> 1 costs 4
        # 3 -> 1 costs 2
        # 0 -> 1 costs 1
        test_utils.test_input_output(
            """
            5
            -5 -3 5 3 0
            """,
            "13",
            solve_func=make_product_equal_one.solve,
            test_case=self,
        )

    def test_example_4(self):
        # same as the test above but instead of moving -3 to -1 we move 3 to 1
        test_utils.test_input_output(
            """
            5
            -5 3 5 3 0
            """,
            "13",
            solve_func=make_product_equal_one.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
