def get_Char(input_string):
    if input_string is None or not input_string.isalpha():
        raise ValueError("Invalid input string")

    sum_ascii = sum(ord(char) - 97 for char in input_string.lower()) % 26
    return chr(97 + sum_ascii)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()