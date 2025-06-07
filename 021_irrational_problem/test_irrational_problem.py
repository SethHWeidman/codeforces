import unittest

import test_utils

import irrational_problem


class TestIrrationalProblem(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            2 7 1 8 2 8
            """,
            """
            0
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            20 30 40 50 0 100
            """,
            """
            20
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            31 41 59 26 17 43
            """,
            """
            9
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            31 41 60 26 18 43
            """,
            """
            8
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            4 2 3 5 50 100
            """,
            """
            0
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            541 931 822 948 131 193
            """,
            """
            63
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            1 2 3 4 1 1
            """,
            """
            0
            """,
            solve_func=irrational_problem.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
