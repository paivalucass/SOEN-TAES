from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    if not strings or not substring:
        return []

    filtered_strings = [s for s in strings if substring in s]

    return filtered_strings
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_with_substring(self):
        input_strings = ['abc', 'bacd', 'cde', 'array']
        expected_output = ['abc', 'bacd', 'array']
        self.assertEqual(filter_by_substring(input_strings, 'a'), expected_output)

if __name__ == '__main__':
    unittest.main()