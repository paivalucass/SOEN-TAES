def get_Char(strr):
    if not strr:
        raise ValueError("Input string cannot be empty")
    total_ASCII_value = sum(ord(char) for char in strr if char.isalpha())
    char_index = (total_ASCII_value % 26) + 97
    return chr(char_index)  # Getting the corresponding character in lowercase
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()