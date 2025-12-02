from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length")
    for char in a:
        if char not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")
    for char in b:
        if char not in ['0', '1']:
            raise ValueError("Input strings must consist only of 1s and 0s")

    result = ""
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