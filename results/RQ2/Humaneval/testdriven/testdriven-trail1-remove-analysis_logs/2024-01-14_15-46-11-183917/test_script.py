from typing import List

def concatenate(strings: List[str]) -> str:
    if not strings or not all(isinstance(s, str) for s in strings):
        return ""
    return ''.join(strings)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()