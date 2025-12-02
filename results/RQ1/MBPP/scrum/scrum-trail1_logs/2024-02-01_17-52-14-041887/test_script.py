def get_Char(input_str):
    if not input_str:
        return "Error: Empty input string"
    for char in input_str:
        if not char.isalpha():
            return "Error: Non-alphabetic characters in input string"
    ascii_sum = sum(ord(char.lower()) - 97 for char in input_str)
    result_char = chr(((ascii_sum % 26) + 97) % 122)
    return result_char
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()