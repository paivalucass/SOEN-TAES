from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_list = [s for s in strings if substring in s]
    return filtered_list
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
    
    def test_with_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

if __name__ == '__main__':
    unittest.main()