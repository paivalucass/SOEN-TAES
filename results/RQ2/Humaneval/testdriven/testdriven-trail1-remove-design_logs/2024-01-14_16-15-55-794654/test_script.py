from typing import List

def concatenate(strings: List[str]) -> str:
    if strings is None:
        return "Error: Input is null"
    if not all(isinstance(s, str) for s in strings):
        return "Error: Input data is not a list of strings"
    if any(',' in s for s in strings):
        return "Error: Invalid input format"
    
    return ''.join(strings)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenation(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()