'''
https://codeforces.com/problemset/problem/68/A
1,100 rated problem
Tough - had to submit several times to figure out the "trick" - interesting problem, you
really have to think about it!
'''


def irrational_problem(nums: list[int], a: int, b: int) -> int:
    min_nums = min(nums)
    if min_nums <= a:
        return 0
    elif min_nums < b:
        return min_nums - a
    else:
        return b - a + 1


def solve():
    ints = list(map(int, input().strip().split()))
    print(irrational_problem(ints[:4], ints[4], ints[5]))


if __name__ == "__main__":
    solve()
