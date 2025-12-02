import re

def text_starta_endb(text):
    if re.search(r'a.*b', text):
        return 'Match found'
    else:
        return 'No match found'

assert text_starta_endb("aabbbb")
import unittest

class Test(unittest.TestCase):
    def test_text_starta_endb(self):
        self.assertTrue(text_starta_endb("aabbbb"))

if __name__ == '__main__':
    unittest.main()