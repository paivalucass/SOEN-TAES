import re

def text_match_wordz(text):
    pattern = r'\b\w*z\w*\b'
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_wordz("pythonz."))

if __name__ == '__main__':
    unittest.main()