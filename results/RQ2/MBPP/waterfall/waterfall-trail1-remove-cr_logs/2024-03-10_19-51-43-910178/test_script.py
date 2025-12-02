def get_char(input_string: str) -> str:
    if not input_string.isalpha():
        raise ValueError("Input string should contain only alphabetic characters")
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty")

    ascii_sum = sum((ord(char) - ord('a')) % 26 for char in input_string.lower())
    result_char = chr(ascii_sum + ord('a'))

    return result_char
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()