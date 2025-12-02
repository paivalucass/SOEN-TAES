import re

def string_xor(a: str, b: str) -> str:
    try:
        if re.match("^[01]*$", a) and re.match("^[01]*$", b):
            if len(a) == len(b):
                result = ""
                for i in range(len(a)):
                    if a[i] == b[i]:
                        result += '0'
                    else:
                        result += '1'
                return result
            else:
                return "Error"
        else:
            return "Error"
    except:
        return "Error"

import unittest

class Test(unittest.TestCase):
    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')

if __name__ == '__main__':
    unittest.main()