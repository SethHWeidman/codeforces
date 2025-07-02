def case_of_fake_numbers(n: int, nums: list[int]) -> bool:
    num_turns = n - nums[0] if nums[0] > 0 else 0
    for i in range(1, n):
        if i % 2 == 1:
            # new value of `nums[i]` after `num_turns` - turning in reverse
            new_val = (nums[i] - num_turns) % n
        else:
            # new value of `nums[i]` after `num_turns` - turning forward
            new_val = (nums[i] + num_turns) % n
        if new_val != i:
            return False

    return True


def solve():
    n = int(input().strip())
    nums = list(map(int, input().strip().split(" ")))
    if case_of_fake_numbers(n, nums):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    solve()
