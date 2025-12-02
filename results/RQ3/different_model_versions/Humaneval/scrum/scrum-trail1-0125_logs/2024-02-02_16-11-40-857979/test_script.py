from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length for XOR operation.")

    if not all(char in ['0', '1'] for char in a + b):
        raise ValueError("Invalid input, only 1s and 0s are allowed")

    result = [str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b)]

    return "".join(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()