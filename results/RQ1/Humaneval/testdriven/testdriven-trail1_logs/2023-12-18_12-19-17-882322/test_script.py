from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise ValueError("Input must be a list of strings")
    if not strings:
        return None
    else:
        longest_string = max(strings, key=len)
        return longest_string
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_longest_string(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_multiple_longest_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()