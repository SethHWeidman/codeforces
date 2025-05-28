import collections


def ilya_tic_tac_toe(board: list[list[str]]) -> str:
    # need to check 20 cases:
    # eight row cases:
    # eight column cases
    # four diagonal cases
    # (missed these initially) four off-diagonal cases

    # row cases
    row_cases = [
        [board[0][0], board[0][1], board[0][2]],
        [board[0][1], board[0][2], board[0][3]],
        [board[1][0], board[1][1], board[1][2]],
        [board[1][1], board[1][2], board[1][3]],
        [board[2][0], board[2][1], board[2][2]],
        [board[2][1], board[2][2], board[2][3]],
        [board[3][0], board[3][1], board[3][2]],
        [board[3][1], board[3][2], board[3][3]],
    ]

    column_cases = [
        [board[0][0], board[1][0], board[2][0]],
        [board[1][0], board[2][0], board[3][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[1][1], board[2][1], board[3][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[1][2], board[2][2], board[3][2]],
        [board[0][3], board[1][3], board[2][3]],
        [board[1][3], board[2][3], board[3][3]],
    ]

    diagonal_cases = [
        [board[0][0], board[1][1], board[2][2]],
        [board[1][1], board[2][2], board[3][3]],
        [board[0][3], board[1][2], board[2][1]],
        [board[1][2], board[2][1], board[3][0]],
    ]

    off_diagonal_cases = [
        [board[0][1], board[1][2], board[2][3]],
        [board[1][3], board[2][2], board[3][1]],
        [board[3][2], board[2][1], board[1][0]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    for case in row_cases + column_cases + diagonal_cases + off_diagonal_cases:
        case_counter = collections.Counter(case)

        if case_counter['x'] == 2 and case_counter['o'] == 0 and case_counter['.'] == 1:
            return 'YES'

    return 'NO'


def solve():
    board = []
    for _ in range(4):
        line_list = []
        line = input().strip()
        for char in line:
            line_list.append(char)
        board.append(line_list)
    print(ilya_tic_tac_toe(board))


if __name__ == "__main__":
    solve()
