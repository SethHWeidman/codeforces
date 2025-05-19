# test_fruits.py
import unittest

import test_utils

import seating_on_bus


class TestSeatingOnBus(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2 7
            """,
            """
            5 1 6 2 7 3 4
            """,
            solve_func=seating_on_bus.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            9 36
            """,
            """
            19 1 20 2 21 3 22 4 23 5 24 6 25 7 26 8 27 9 28 10 29 11 30 12 31 13 32 14 33 15 34 16 35 17 36 18
            """,
            solve_func=seating_on_bus.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
