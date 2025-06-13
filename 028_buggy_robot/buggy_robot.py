'''
https://codeforces.com/problemset/problem/888/B
Solved in ~15 mins on 6/13/25
'''

import collections


def buggy_robot(n: int, sequence: str) -> int:
    cnts = collections.defaultdict(int)

    max_moves_back_to_center = 0

    for i in range(n):
        move = sequence[i]
        cnts[move] += 1

        new_maximum = min(cnts['D'], cnts['U']) * 2 + min(cnts['L'], cnts['R']) * 2
        max_moves_back_to_center = max(max_moves_back_to_center, new_maximum)

    return max_moves_back_to_center


def solve():
    n = int(input().strip())
    sequence = input().strip()
    print(buggy_robot(n, sequence))


if __name__ == "__main__":
    solve()
