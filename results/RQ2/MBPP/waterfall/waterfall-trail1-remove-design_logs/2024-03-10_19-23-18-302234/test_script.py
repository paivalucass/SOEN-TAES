import re
def text_match_wordz_middle(text):
    return bool(re.search(r'\Bz\B', text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()