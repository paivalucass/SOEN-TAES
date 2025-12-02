import re

def text_starta_endb(text):
    pattern = 'a.*b$'
    if re.match(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_starta_endb('aabbbb'))

if __name__ == '__main__':
    unittest.main()