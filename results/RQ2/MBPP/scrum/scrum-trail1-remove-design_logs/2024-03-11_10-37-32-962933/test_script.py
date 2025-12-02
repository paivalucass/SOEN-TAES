def text_match_one(text):
    if 'a' in text and 'b' in text:
        if text.index('a') < text.index('b'):
            return True
    return False
import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()