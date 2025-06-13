"""
https://codeforces.com/problemset/problem/1295/A
Solved in ~15 mins on 6/12/25
"""


def display_the_number(n: int) -> str:
    '''
    Just using 1s and 7s gives you the largest number
    '''
    if n % 2 == 0:
        num_list = ['1'] * (n // 2)
    if n % 2 == 1:
        num_list = ['7'] + ['1'] * (int(n // 2) - 1)

    num_str = "".join(num_list)
    return num_str


def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(display_the_number(n))


if __name__ == '__main__':
    solve()
