import unittest

import test_utils

import ilya_tic_tac_toe


class TestIlyaTicTacToe(unittest.TestCase):
    def test_official_cases(self):
        test_utils.test_input_output(
            """
            xx..
            .oo.
            x...
            oox.
            """,
            """
            YES
            """,
            solve_func=ilya_tic_tac_toe.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            x.ox
            ox..
            x.o.
            oo.x
            """,
            """
            NO
            """,
            solve_func=ilya_tic_tac_toe.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            x..x
            ..oo
            o...
            x.xo
            """,
            """
            YES
            """,
            solve_func=ilya_tic_tac_toe.solve,
            test_case=self,
        )

        test_utils.test_input_output(
            """
            o.x.
            o...
            .x..
            ooxx
            """,
            """
            NO
            """,
            solve_func=ilya_tic_tac_toe.solve,
            test_case=self,
        )


if __name__ == "__main__":
    unittest.main()
