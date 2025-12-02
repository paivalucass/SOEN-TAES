def text_match_wordz_middle(text):
    if len(text) < 3:
        return False
    else:
        middle_text = text[1:-1]
        if 'z' in middle_text:
            return True
        else:
            return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()