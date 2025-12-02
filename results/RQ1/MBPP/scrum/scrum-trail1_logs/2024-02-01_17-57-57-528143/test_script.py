import re
def text_match_wordz(text):
    word_list = re.findall(r'\b\w*z\w*\b', text, re.IGNORECASE)
    if word_list:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()