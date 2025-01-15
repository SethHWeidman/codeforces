import sys


class Solution:
    def minimal_cost_to_product_one(self, numbers: list[int]) -> int:
        """
        Given a list of integers `numbers`, returns the minimal cost (number of +/-1
        operations) required to make their product = 1.
        """
        total_cost = 0
        neg_count = 0
        zero_count = 0

        for a in numbers:
            if a == 0:
                # Cost to move 0 -> ±1 is 1
                total_cost += 1
                zero_count += 1
            elif a > 0:
                # Cost to become +1 is (a - 1)
                total_cost += a - 1
            else:  # a < 0
                # Cost to become -1 is (-a - 1)
                total_cost += -a - 1
                neg_count += 1

        # Fix sign parity if needed
        if neg_count % 2 != 0:
            # If there's at least one zero, we can pick it to be -1 with no extra cost
            if zero_count == 0:
                # Must flip exactly one from +1 to -1 or vice versa (cost = 2)
                total_cost += 2

        return total_cost


def solve():
    _ = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    s = Solution()
    answer = s.minimal_cost_to_product_one(numbers)
    print(answer)


if __name__ == "__main__":
    solve()
