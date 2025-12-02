from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    filtered_strings = [s for s in strings if substring in s]
    return filtered_strings
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

if __name__ == '__main__':
    unittest.main()