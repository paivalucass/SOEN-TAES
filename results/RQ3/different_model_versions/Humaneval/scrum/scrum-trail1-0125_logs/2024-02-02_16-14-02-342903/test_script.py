from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    if not isinstance(strings, list) or not all(isinstance(x, str) for x in strings):
        raise TypeError("Input strings must be a list of strings")
    if not isinstance(prefix, str):
        raise TypeError("Prefix must be a string")

    filtered_list = [s for s in strings if s.lower().startswith(prefix.lower())]

    return filtered_list
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()