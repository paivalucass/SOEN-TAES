from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    """

    if not strings:
        return None

    max_length = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_length]

    return longest_strings[-1] if len(longest_strings) == 1 else max(longest_strings, key=len)
import unittest

class Test(unittest.TestCase):
    def test_longest_empty_list(self):
        self.assertIsNone(longest([]))

    def test_longest_single_character_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_multiple_character_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()