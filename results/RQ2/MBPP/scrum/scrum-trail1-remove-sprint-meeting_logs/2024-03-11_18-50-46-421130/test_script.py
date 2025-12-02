def replace_char(str1, ch, newch):
    if not str1 or not ch or not newch:
        return "Error: original string, character to be replaced, and new character must be provided"
    
    return str1.replace(ch, newch)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()