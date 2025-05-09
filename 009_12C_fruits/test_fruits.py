# test_fruits.py
import unittest
import test_utils
import fruits


class TestFruits(unittest.TestCase):
    def test_official_cases(self):
        # sample 1
        test_utils.test_input_output(
            """
            5 3
            4 2 1 10 5
            apple
            orange
            mango
            """,
            """
            7 19
            """,
            solve_func=fruits.solve,
            test_case=self,
        )
        # sample 2
        test_utils.test_input_output(
            """
            6 5
            3 5 1 6 8 1
            peach
            grapefruit
            banana
            orange
            orange
            """,
            """
            11 30
            """,
            solve_func=fruits.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
