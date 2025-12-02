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
    if strings:
        return max(strings, key=lambda x: len(x))
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test_longest_empty_list(self):
        self.assertIsNone(longest([]))

    def test_longest_single_char_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_multiple_char_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()