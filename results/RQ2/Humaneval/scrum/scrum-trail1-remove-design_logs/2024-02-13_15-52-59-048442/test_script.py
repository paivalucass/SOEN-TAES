from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        return "Error: Invalid input strings"

    result = ""
    for i in range(len(a)):
        if a[i] != "0" and a[i] != "1" or b[i] != "0" and b[i] != "1":
            return "Error: Invalid input strings"
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