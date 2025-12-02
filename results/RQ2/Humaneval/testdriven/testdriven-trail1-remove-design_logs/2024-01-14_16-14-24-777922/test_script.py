from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = 0
    longest_string = None
    for s in strings:
        if isinstance(s, str):
            if len(s) > max_len:
                max_len = len(s)
                longest_string = s
    return longest_string

# Test Cases:
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(longest(['@', '!', '#']))  # '@'
import unittest

class Test(unittest.TestCase):
    def test_longest_empty_list(self):
        self.assertIsNone(longest([]))

    def test_longest_single_character_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_different_length_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()