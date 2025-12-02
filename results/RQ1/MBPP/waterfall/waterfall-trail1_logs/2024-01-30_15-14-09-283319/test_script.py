import re

def text_starta_endb(text):
    pattern = re.compile(r'a.*b$')
    if pattern.match(text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_starta_endb('aabbbb'), True)

if __name__ == '__main__':
    unittest.main()