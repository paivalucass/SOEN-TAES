from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_len]
    return longest_strings[0]
import unittest
from typing import List, Optional

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')
        self.assertEqual(longest(['aaa', 'bbb', 'c']), 'aaa')

if __name__ == '__main__':
    unittest.main()