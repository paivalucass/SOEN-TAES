from typing import List

def string_xor(a: str, b: str) -> str:
    if not all(char in '01' for char in a) or not all(char in '01' for char in b):
        return "Input validation error"
    
    if len(a) != len(b):
        return "Input length mismatch error"
    
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()