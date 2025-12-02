from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # input validation to check if the input list is not empty
        return None
    else:
        return max(strings, key=len)  # Using a built-in function to find the longest string in the list

# Testing with an empty list input
assert longest([]) == None

# Testing with a list of strings with the same length
assert longest(['aa', 'bb', 'cc']) == 'aa'

# Testing with a list of strings with different lengths
assert longest(['a', 'bb', 'ccc']) == 'ccc'
import unittest

class Test(unittest.TestCase):
    def test_longest_empty_list(self):
        self.assertEqual(longest([]), None)

    def test_longest_single_character_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_multiple_character_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()