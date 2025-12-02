from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    if not strings:
        return []

    filtered_strings = [s for s in strings if s.startswith(prefix)]
    return filtered_strings
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    
    def test_prefix_a(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()