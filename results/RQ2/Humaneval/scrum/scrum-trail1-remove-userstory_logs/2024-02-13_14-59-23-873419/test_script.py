from typing import List

def string_xor(a: str, b: str) -> str:
    result = ""
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result

import unittest

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()