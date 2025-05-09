'''
https://codeforces.com/problemset/problem/1206/B
'''

import sys


def minimal_cost_to_product_one(numbers: list[int]) -> int:
    '''
    Idea:

    * If a number `x` is positive, we can make it 1 with `x - 1` moves
    * If a number `x` is negative, we can make it -1 with `-x - 1` moves
    * If a number is 0, we can make it 1 with 1 move

    * If we have an odd number of negative numbers, we can flip 0 to be -1 (instead of 1)
      with no cost
        * If we have no zeros, we have to add two to the total cost
    '''
    total_cost = 0
    num_negative = 0
    num_zeros = 0

    for n in numbers:
        if n > 0:
            total_cost += n - 1

        elif n < 0:
            total_cost += -n - 1
            num_negative += 1

        else:
            total_cost += 1
            num_zeros += 1

    if num_negative % 2 == 1:

        if num_zeros == 0:

            total_cost += 2

    return total_cost


def solve():
    '''
    ChatGPT wrote this
    '''
    _ = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    answer = minimal_cost_to_product_one(numbers)
    print(answer)


if __name__ == "__main__":
    solve()
