from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_strings = []
    for s in strings:
        if substring in s:
            filtered_strings.append(s)
    return filtered_strings

import unittest

from typing import List


class Test(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
        
    def test_with_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])


if __name__ == '__main__':
    unittest.main()