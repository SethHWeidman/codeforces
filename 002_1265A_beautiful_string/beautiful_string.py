"""
https://codeforces.com/problemset/problem/1265/A
"""

import sys

ALLOWED_CHARS = ['a', 'b', 'c']


def make_beautiful_string(s: str) -> str:
    """
    Replaces each '?' in the input string with one of `ALLOWED_CHARS` so that no two
    consecutive characters are the same. Returns the modified string, or "-1" if it’s
    impossible to achieve a beautiful string.

    Idea:
      1. Scan the original string for any adjacent non-'?' duplicates; if found, no
         replacements can fix that, so return "-1".
      2. Build a new list `new_string` by iterating over each index `i`:
         - If `s[i]` is not '?', append it unchanged.
         - If `s[i]` is '?':
             • If `i == 0`, choose any allowed character different from `s[1]`.
             • Otherwise (`i < len(s)`), choose any allowed character different from the
               previously appended character (`new_string[i-1]`) and from the next
               character in the original string (`s[i+1]`).
      3. Join `new_string` into `candidate_string`.
      4. Perform a final scan for adjacent duplicates in `candidate_string`; if any are
         found, return "-1", otherwise return `candidate_string`.
    """
    n = len(s)
    # initial check to see if strings cannot be beautified
    for i in range(n - 1):
        if s[i] != '?' and s[i + 1] != '?' and s[i] == s[i + 1]:
            return "-1"

    new_string = []

    for i, char in enumerate(s):
        if char != "?":
            new_string.append(char)
            continue

        # after this point, `char` is "?"
        if i == 0:
            bad_char = s[i + 1]
            for allowed_char in ALLOWED_CHARS:
                if allowed_char != bad_char:
                    new_string.append(allowed_char)
                    break

        elif i < len(s):
            bad_chars = [new_string[i - 1], s[i + 1]]
            for allowed_char in ALLOWED_CHARS:
                if allowed_char not in bad_chars:
                    new_string.append(allowed_char)
                    break

        else:
            bad_char = new_string[i - 1]
            for allowed_char in ALLOWED_CHARS:
                if allowed_char != bad_char:
                    new_string.append(allowed_char)
                    break

    candidate_string = "".join(new_string)

    # final check
    for i in range(n - 1):
        if candidate_string[i] == candidate_string[i + 1]:
            return "-1"

    return candidate_string


def solve():
    """Reads input and processes each test case."""
    f = sys.stdin.readline
    t = int(f().strip())
    for _ in range(t):
        s = f().strip()
        print(make_beautiful_string(s))


if __name__ == "__main__":
    solve()
