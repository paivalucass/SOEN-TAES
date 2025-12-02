def get_Char(strr):
    total_ascii = 0
    for char in strr:
        if char.isalpha():
            total_ascii += ord(char) - 97
    resulting_char = chr(((total_ascii % 26) + 97)%123)
    if resulting_char < 'a':
        return chr(ord(resulting_char) + 26)
    return resulting_char
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Char('abc'), 'f')

if __name__ == '__main__':
    unittest.main()