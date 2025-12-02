import re
import unittest

def text_match_one(text):
    pattern = 'ab+'
    if re.search(pattern, text):
        return True
    else:
        return False

class Test(unittest.TestCase):
    def test_text_match_one(self):
        self.assertFalse(text_match_one("ac"))

if __name__ == '__main__':
    unittest.main()
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()