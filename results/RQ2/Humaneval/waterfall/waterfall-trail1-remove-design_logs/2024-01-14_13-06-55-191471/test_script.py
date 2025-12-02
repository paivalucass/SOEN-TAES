from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: List of strings to concatenate
    :return: Concatenated string
    """
    return ''.join(strings)
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()