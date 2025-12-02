from typing import List


def validate_input(a: str, b: str) -> bool:
    """ Input are two strings a and b. Ensure that they consist only of 1s and 0s. Return True if the inputs are valid, False otherwise.
    >>> validate_input('010', '110')
    True
    """
    if set(a) <= {'0', '1'} and set(b) <= {'0', '1'}:
        return True
    return False


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if not validate_input(a, b):
        raise ValueError('Input must consist only of 1s and 0s')
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result
import unittest

from typing import List

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('1111', '0000'), '1111')
        self.assertEqual(string_xor('101010', '111111'), '010101')
        self.assertEqual(string_xor('1001', '0101'), '1100')

if __name__ == '__main__':
    unittest.main()