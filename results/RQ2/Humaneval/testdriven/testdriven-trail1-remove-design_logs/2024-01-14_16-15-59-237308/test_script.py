from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.
    :param strings: List of strings to filter
    :param prefix: Prefix to filter strings by
    :return: List of strings that start with the given prefix
    :raises ValueError: If input list contains non-string elements
    """

    if not all(isinstance(s, str) for s in strings):
        raise ValueError("Input list must contain only strings")

    return [s for s in strings if s.startswith(prefix)]
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_by_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

if __name__ == '__main__':
    unittest.main()