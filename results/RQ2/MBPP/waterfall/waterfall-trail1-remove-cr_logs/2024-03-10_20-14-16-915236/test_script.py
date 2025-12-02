import re
def text_match_wordz_middle(text):
    pattern = r'\b\w*z\w+\b'
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle("pythonzabc."), True)

if __name__ == '__main__':
    unittest.main()