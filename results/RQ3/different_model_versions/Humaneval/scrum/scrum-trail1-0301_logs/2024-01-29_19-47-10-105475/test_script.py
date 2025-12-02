from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    """
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings) or not isinstance(substring, str) or not substring:
        return []

    return [s for s in strings if substring in s]
import unittest

from typing import List

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_substring_not_present(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'j'), [])

    def test_substring_present(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

if __name__ == '__main__':
    unittest.main()