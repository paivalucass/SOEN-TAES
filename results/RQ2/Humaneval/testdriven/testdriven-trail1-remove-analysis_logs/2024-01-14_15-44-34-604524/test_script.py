from typing import List

def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Input validation
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        raise ValueError("Invalid input: Input strings should consist only of 1s and 0s")

    if len(a) != len(b):
        raise ValueError("Unequal length strings: Input strings should have equal length")

    # Perform binary XOR operation
    result = ''.join(str(int(i) ^ int(j)) for i, j in zip(a, b))

    return result
import unittest

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()