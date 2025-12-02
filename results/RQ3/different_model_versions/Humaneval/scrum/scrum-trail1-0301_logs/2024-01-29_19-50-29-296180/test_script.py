from typing import List

def concatenate(strings: List[str]) -> str:
    if not isinstance(strings, list):
        raise TypeError("Input is not a list.")
    if not strings:
        return ""
    for string in strings:
        if not isinstance(string, str):
            raise TypeError("List contains non-string type.")
    return ''.join(strings)
import unittest
from typing import List

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenation(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()