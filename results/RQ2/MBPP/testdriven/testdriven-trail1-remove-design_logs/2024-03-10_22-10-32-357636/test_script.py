def replace_char(str1, ch, newch):
    if not str1 or not ch or not newch:
        return "Input string and characters to be replaced and new characters are required."
    try:
        return str1.replace(ch, newch)
    except ValueError:
        return "Character to be replaced is not found in the input string."
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()