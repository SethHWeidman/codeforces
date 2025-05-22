import sys


def binary_cafe(n: int, k: int) -> int:
    # the LLM reminded me that we can't compute 2**k for large `k``; the problem notes
    # that `n`` will not be greater than 10^9, so we can hardcode the solution for `k`
    # sufficiently large
    if k >= 31:
        return n + 1
    elif n / 2 >= 2 ** (k - 1):
        return 2**k
    else:  # 2 ** (k - 1) > n / 2
        return n + 1


def solve():
    num_cases = int(sys.stdin.readline().strip())
    for _ in range(num_cases):
        n, k = map(int, sys.stdin.readline().strip().split())
        # the LLM reminded me that more consistent with the use of `sys` above would be
        # to use `sys.stdout.write`
        print(binary_cafe(n, k))


if __name__ == "__main__":
    solve()
