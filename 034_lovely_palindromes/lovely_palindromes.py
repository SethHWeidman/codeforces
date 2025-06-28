def lovely_palindromes(n_str: str) -> str:
    # first nine are 11, ..., 99
    # then next ten are 1001, 1111, 1221, ..., 1991
    # next ten are 2002, 2112, etc.

    return n_str + n_str[::-1]


def solve():
    # unlike usual: not converting this to an int
    n = input().strip()
    print(lovely_palindromes(n))


if __name__ == "__main__":
    solve()
