from typing import List

def concatenate(strings: List[str]) -> str:
    if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
        raise TypeError("Input parameter 'strings' must be a list of strings")
    
    if not strings:
        return ''
    
    return ''.join(strings)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenation(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()