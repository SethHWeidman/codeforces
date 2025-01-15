import io
import textwrap
import typing
import unittest
from unittest import mock


def _dedent_and_remove_leading_blank_line(text: str) -> str:
    """
    1. Dedent the given string (so that code indentation doesn't break spacing).
    2. If the *first line* is blank (or just spaces), remove it.
    3. Return the cleaned string.
    """
    dedented = textwrap.dedent(text)
    lines = dedented.splitlines()
    if lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines)


def test_input_output(
    input_data: str,
    expected_output: str,
    solve_func: typing.Callable,
    test_case: unittest.TestCase,
) -> None:
    """
    Utility that:
      1. Dedents and cleans up `input_data`.
      2. Mocks stdin / stdout.
      3. Calls the `solve_func`.
      4. Asserts that solve_func()'s stdout matches `expected_output`.
    """
    input_data = _dedent_and_remove_leading_blank_line(input_data)

    with mock.patch('sys.stdin', io.StringIO(input_data)), mock.patch(
        'sys.stdout', new_callable=io.StringIO
    ) as stdout_buf:
        solve_func()
        actual_output = stdout_buf.getvalue().strip()

    # Compare
    test_case.assertEqual(actual_output, expected_output)
