from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    if not strings or not prefix:
        return []
    
    return [s for s in strings if s.startswith(prefix)]
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_filter_by_prefix_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_by_prefix_non_empty_list(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()