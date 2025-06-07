'''
https://codeforces.com/problemset/problem/742/A
1000-rated problem
Solved in 10 minutes on 6/6/25
'''

import sys


def arpa_hard_exam(n: int) -> int:
    # the answer is equivalent to returning the remainder when 8 ^ n % 10
    # this cycles through:
    #
    # 8 ^ 1 % 10 = 8
    # 8 ^ 2 = 64 % 10 = 4
    # 8 ^ 3 = 512 % 10 = 2
    # 8 ^ 4 = 4096 % 10 = 6
    #
    # this is because ((10 + x) ^ n) % 10 = (x ^ n) % 10

    # initially forgot this case!
    if n == 0:
        return 1
    if n % 4 == 1:
        return 8
    elif n % 4 == 2:
        return 4
    elif n % 4 == 3:
        return 2
    elif n % 4 == 0:
        return 6


def solve():
    n = int(sys.stdin.read())
    sys.stdout.write(str(arpa_hard_exam(n)))


if __name__ == "__main__":
    solve()
