def burenka_fractions(a: int, b: int, c: int, d: int) -> int:
    '''
    Idea: this is equivalent to asking if `ad == bc`


        * If `a` or `c` is 0, 1
        * If `ac % bd` is 0 or `bd % ac` is 0, 1
        * Otherwise, 2
    '''
    if a == 0 or c == 0:
        return 1

    ad = a * d
    bc = b * c

    if ad == bc:
        return 0

    if ad % bc == 0 or ad % bc == 0:
        return 1

    return 2


def solve():
    n = int(input().strip())
    for _ in range(n):
        line = input().strip().split()
        ints = [int(num) for num in line]
        print(burenka_fractions(ints[0], ints[1], ints[2], ints[3]))


if __name__ == "__main__":
    solve()
