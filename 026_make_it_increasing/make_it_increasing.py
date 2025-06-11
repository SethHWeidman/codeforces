'''
https://codeforces.com/problemset/problem/1675/B
I did not figure this 900-rated problem out without asking ChatGPT for a hint
'''


def make_it_increasing(n: int, nums: list[int]) -> int:
    is_increasing = True
    for i in range(n - 1):
        if nums[i] >= nums[i + 1]:
            is_increasing = False
    if is_increasing:
        return 0

    i = n - 1
    num_divisions = 0
    while i > 0:
        greater_element = nums[i]
        lesser_element = nums[i - 1]
        # start the halving
        while lesser_element >= greater_element and lesser_element > 0:
            lesser_element = int(lesser_element / 2)
            num_divisions += 1
        # edge case: if both `greater_element` and `lesser_element` end up as 0, there
        # must be no way to make the sequence increasing, so we exit
        if greater_element == 0 and lesser_element == 0:
            return -1
        nums[i - 1] = lesser_element
        i -= 1
    return num_divisions


def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        nums = list(map(int, input().strip().split()))
        print(make_it_increasing(n, nums))


if __name__ == '__main__':
    solve()
