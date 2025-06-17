""" """


def initial_bet(coins: list[str]) -> int:
    s = sum(coins)
    # forgot about this case initially...
    if s == 0:
        return -1
    if s % 5 == 0:
        return int(s // 5)
    return -1


def solve():
    coins = list(map(int, input().strip().split()))
    print(initial_bet(coins))


if __name__ == "__main__":
    solve()
