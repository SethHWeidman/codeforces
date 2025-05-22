import io
import textwrap
import typing
import unittest
from unittest import mock


def _clean_multiline_string(text: str) -> str:
    """
    1. Dedent the given string (removes common leading whitespace).
    2. Split into lines.
    3. If the first line is blank (contains only whitespace), remove it.
    4. Join the lines back together with newline characters.
    5. Strip any leading or trailing whitespace from the entire resulting string.
    """
    dedented = textwrap.dedent(text)
    lines = dedented.splitlines()
    # Remove the first line only if it exists and is effectively blank
    if lines and not lines[0].strip():
        lines.pop(0)
    # Join the potentially modified lines and strip whitespace from the whole block
    return "\n".join(lines).strip()


def test_input_output(
    input_data: str,
    expected_output: str,
    solve_func: typing.Callable,
    test_case: unittest.TestCase,
) -> None:
    """
    Utility that:
      1. Cleans up `input_data` (dedent, remove leading blank line, strip).
      2. Cleans up `expected_output` (dedent, remove leading blank line, strip).
      3. Mocks sys.stdin and sys.stdout.
      4. Calls the provided `solve_func`.
      5. Asserts that the stripped stdout from solve_func() matches the cleaned `expected_output`.
    """
    # Clean both input and expected output using the helper function
    cleaned_input = _clean_multiline_string(input_data)
    # Apply cleaning here too!
    cleaned_expected_output = _clean_multiline_string(expected_output)

    with mock.patch('sys.stdin', io.StringIO(cleaned_input)), mock.patch(
        'sys.stdout', new_callable=io.StringIO
    ) as stdout_buf:
        solve_func()
        # Get the actual output and strip it for comparison
        actual_output = stdout_buf.getvalue().strip()

    # Compare the stripped actual output with the cleaned expected output
    test_case.assertEqual(actual_output, cleaned_expected_output)
