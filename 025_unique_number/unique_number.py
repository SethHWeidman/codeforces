'''
https://codeforces.com/problemset/problem/1462/C
900 rated problem, solved on the first try on 6/9/25
'''


def unique_number(x: int) -> int:

    new_number = []
    i = 9
    while i > 0 and x > 0:
        if x > i:
            new_number.insert(0, str(i))
        else:
            new_number.insert(0, str(x))
        x -= i
        i -= 1

    return int("".join(new_number)) if x <= 0 else -1


def solve():
    a = int(input().strip())
    for _ in range(a):
        i = int(input().strip())
        print(unique_number(i))


if __name__ == "__main__":
    solve()
