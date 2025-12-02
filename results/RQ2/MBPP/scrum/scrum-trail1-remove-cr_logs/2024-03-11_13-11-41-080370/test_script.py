from typing import Union

def check_char(string: str) -> Union[str, ValueError]:
    if len(string) == 0:
        raise ValueError("Input string cannot be empty")

    return "Valid" if string[0] == string[-1] else "Invalid"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_char('abba'), "Valid")

if __name__ == '__main__':
    unittest.main()