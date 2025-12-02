from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise TypeError("Input should be a list of strings")

    if not strings:
        return None

    longest_string = max(strings, key=len)
    return longest_string
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_multiple_strings_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()