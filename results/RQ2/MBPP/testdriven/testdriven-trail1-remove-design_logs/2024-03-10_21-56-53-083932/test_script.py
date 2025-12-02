def get_char(strr):
    '''
    Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.
    assert get_char("abc") == "f"
    '''
    if not strr.isalpha() or len(strr) == 0 or len(strr) > 100:
        return "Error message indicating invalid input"
    total_ascii = sum(ord(char) for char in strr)
    return chr(((total_ascii % 26) + 97) if total_ascii else 97)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()