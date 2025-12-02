from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = max(len(s) for s in strings)
    longest_strings = [s for s in strings if len(s) == max_length]
    return longest_strings[0] if longest_strings else None
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