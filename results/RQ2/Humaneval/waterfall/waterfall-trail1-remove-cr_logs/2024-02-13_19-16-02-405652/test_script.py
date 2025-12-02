from typing import List

def concatenate(strings: List[str]) -> str:
    if not strings:
        return ''

    result = ''.join(strings)

    return result
import unittest

class Test(unittest.TestCase):
    def test_concatenate_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_list_of_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()