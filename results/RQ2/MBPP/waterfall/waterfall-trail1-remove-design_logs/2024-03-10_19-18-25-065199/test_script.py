def replace_char(str1, ch, newch):
    if not str1 or not ch or not newch:
        return "Input string and characters to be replaced cannot be empty"
    
    import re
    return re.sub(ch, newch, str1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(replace_char("polygon", 'y', 'l'), "pollgon")

if __name__ == '__main__':
    unittest.main()