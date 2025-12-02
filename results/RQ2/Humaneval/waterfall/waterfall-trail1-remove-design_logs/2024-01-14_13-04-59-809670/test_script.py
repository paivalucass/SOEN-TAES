from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings or not all(isinstance(s, str) for s in strings):
        return None
    
    max_length = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_length]
    return longest_strings[0]

import unittest

class Test(unittest.TestCase):
    def test_empty_input(self):
        self.assertIsNone(longest([]))
    
    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()