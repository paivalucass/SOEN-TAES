def get_char(strr):
    if not isinstance(strr, str):
        return "Error: Invalid input, please provide a string"
    if len(strr) == 0:
        return "Error: Empty input, please provide a non-empty string"
    if not all(char.isalpha() for char in strr):
        return "Error: Invalid input, please provide a string containing only alphabetic characters"
    if len(strr) == 1:
        return "Error: Invalid input, please provide a string containing more than one character"
    
    sum_ascii = sum(ord(c) - 97 for c in strr.lower() if c.isalpha())
    remainder = sum_ascii % 26
    result = chr(remainder + 97)  # converting the remainder back to a character using the ASCII table
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()