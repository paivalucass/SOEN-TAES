from typing import List

def string_xor(a: str, b: str) -> str:
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        raise ValueError("Input strings should consist only of 1s and 0s")

    if len(a) != len(b):
        raise ValueError("Input strings should be of equal length")

    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    return result
import unittest

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()