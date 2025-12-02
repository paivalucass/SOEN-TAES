def text_match_wordz(text):
    import re

    text = text.lower()

    if re.search(r'\b\w*z\w*\b', text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()