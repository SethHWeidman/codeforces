import math


def different_divisors(d: int) -> int:

    def _get_next_prime(n: int) -> int:
        candidate = n + 1
        while True:
            if _is_prime(candidate):
                return candidate
            candidate += 1

    def _is_prime(n: int) -> int:
        for divisor in range(2, round(math.sqrt(n)) + 1):
            if n % divisor == 0:
                return False
        return True

    second_divisor = _get_next_prime(d)
    third_divisor = _get_next_prime(second_divisor + d - 1)
    return second_divisor * third_divisor


def solve():
    num_test_cases = int(input().strip())
    for _ in range(num_test_cases):
        d = int(input().strip())
        print(different_divisors(d))


if __name__ == "__main__":
    solve()
