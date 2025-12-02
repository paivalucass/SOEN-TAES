def text_match_one(text):
    text = text.lower()
    
    if 'a' in text and 'b' in text[text.index('a'):]:
        return True
    else:
        return False

import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_one('ac'), False)

if __name__ == '__main__':
    unittest.main()