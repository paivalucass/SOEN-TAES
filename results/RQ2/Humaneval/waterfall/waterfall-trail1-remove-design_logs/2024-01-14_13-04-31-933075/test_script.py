from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    if not strings or not substring:
        return []

    filtered_strings = [s for s in strings if substring in s]

    return filtered_strings
import unittest

from typing import List


class Test(unittest.TestCase):
    def test_filter_by_substring_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_filter_by_substring_with_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])


if __name__ == '__main__':
    unittest.main()