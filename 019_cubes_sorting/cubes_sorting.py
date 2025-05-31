'''
https://codeforces.com/problemset/problem/1420/A
900 rated CodeForces problem with a fun trick
'''


def cubes_sorting(n: int, cubes: list[int]) -> bool:
    '''
    If the list is sorted in decreasing order (no ties), return False
    Else, return True
    '''
    for i in range(n - 1):
        if cubes[i + 1] >= cubes[i]:
            return True
    return False


def solve():
    num_cases = int(input().strip())
    for _ in range(num_cases):
        n = int(input().strip())
        cubes = list(map(int, input().strip().split()))
        cubes_sorted = cubes_sorting(n, cubes)
        if cubes_sorted:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
