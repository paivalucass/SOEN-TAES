from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings) or not isinstance(substring, str):
        raise TypeError("Input must be a list of strings and substring must be a string")

    if not substring:
        return []

    filtered_list = [string for string in strings if substring in string]

    return filtered_list
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])
    
    def test_normal_case(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

if __name__ == '__main__':
    unittest.main()