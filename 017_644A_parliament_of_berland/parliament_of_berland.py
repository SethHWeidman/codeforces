def parliament_of_berland(
    n_parliamentarians: int, n_rows: int, n_columns: int
) -> list[list[int]] | int:
    total_seats = n_rows * n_columns

    if n_parliamentarians > total_seats:
        return -1

    parliamentarians = range(1, n_parliamentarians + 1)
    odds = [x for x in parliamentarians if x % 2 == 1]
    evens = [x for x in parliamentarians if x % 2 == 0]

    odds_index = 0
    evens_index = 0

    # figure out the arrangement
    seats = [[None] * n_columns for _ in range(n_rows)]
    for row in range(n_rows):
        for column in range(n_columns):
            total_index = row + column
            if total_index % 2 == 0 and odds_index < len(odds):
                seats[row][column] = odds[odds_index]
                odds_index += 1
            elif total_index % 2 == 1 and evens_index < len(evens):
                seats[row][column] = evens[evens_index]
                evens_index += 1
            else:
                seats[row][column] = 0

    return seats


def solve():
    n, a, b = map(int, input().strip().split())
    result = parliament_of_berland(n, a, b)
    if result == -1:
        print(-1)
    elif isinstance(result, list):
        for line in result:
            string_line = [str(x) for x in line]
            print(" ".join(string_line))


if __name__ == "__main__":
    solve()
