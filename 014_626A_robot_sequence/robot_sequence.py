'''
Solved in ~30 minutes on 5/22/25
1,000 rated problem
'''

import collections


def robot_sequence(n: int, sequence: str) -> int:
    num_balanced_slices = 0

    start = 0

    for start in range(n - 1):
        for length in range(2, n + 1 - start):
            slice = sequence[start : start + length]

            # is slice balanced
            counter = collections.defaultdict(int)
            for command in slice:
                counter[command] += 1
            if counter['U'] == counter['D'] and counter['R'] == counter['L']:
                num_balanced_slices += 1

    return num_balanced_slices


def solve():
    n = int(input().strip())
    sequence = input().strip()
    print(robot_sequence(n, sequence))


if __name__ == "__main__":
    solve()
