from typing import List

def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
import unittest

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenating_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()