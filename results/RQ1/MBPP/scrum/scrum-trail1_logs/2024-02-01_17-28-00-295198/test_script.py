import unittest

def text_match_one(text):
    text = text.lower()
    
    if not text:
        return False
    
    for i in range(len(text)):
        if text[i] == 'a' and 'b' in text[i+1:]:
            return True
    return False

class Test(unittest.TestCase):
    def test_text_match_one(self):
        self.assertEqual(text_match_one("ac"), False)

if __name__ == '__main__':
    unittest.main()
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()