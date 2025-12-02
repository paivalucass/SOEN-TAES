import re

def text_starta_endb(text):
    pattern = r'^a.*b$'
    return bool(re.match(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test_starta_endb(self):
        self.assertTrue(text_starta_endb('aabbbb'))

if __name__ == '__main__':
    unittest.main()