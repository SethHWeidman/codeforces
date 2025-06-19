"""
https://codeforces.com/problemset/problem/1146/B
1100-rated CodeForces problem. Had to ask ChatGPT for a hint to properly handle an edge
case.
"""


def hate_a(s: str) -> str:
    '''
    Core idea: `non_a_str_chars` (see below) must have:
        * even length
        * first half of "non a" characters equal to second half

    Turns out there's a tricky edge case with this! See the comment below about the
    branch I had to add after ChatGPT gave me a hint
    '''
    if s.endswith('a') and (len(s) > 1 and s[-2] != 'a'):
        return ':('
    non_a_str_chars = []
    non_a_str_chars_indices = []
    for i, char in enumerate(s):
        if char != 'a':
            non_a_str_chars.append(char)
            non_a_str_chars_indices.append(i)

    num_non_a_chars = len(non_a_str_chars)
    if num_non_a_chars % 2 != 0:
        return ':('

    half_non_a_str_chars = int(num_non_a_chars / 2)
    second_half_non_a_str_chars = non_a_str_chars[half_non_a_str_chars:]
    if non_a_str_chars[:half_non_a_str_chars] != second_half_non_a_str_chars:
        return ':('
    else:
        start_of_second_half_non_a_chars = (
            non_a_str_chars_indices[half_non_a_str_chars]
            if len(non_a_str_chars_indices)
            else len(s)
        )
        # I missed this branch initially - had to ask ChatGPT for a hint on why my code
        # was failing. Strings like "bcbac" will return e.g. "bc" without the next two
        # lines, when they should actually return ":("
        if 'a' in s[start_of_second_half_non_a_chars:]:
            return ':('
        return s[:start_of_second_half_non_a_chars]


def solve():
    s = input().strip()
    print(hate_a(s))


if __name__ == "__main__":
    solve()
