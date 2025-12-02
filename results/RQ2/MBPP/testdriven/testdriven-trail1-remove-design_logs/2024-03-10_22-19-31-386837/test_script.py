import re

def text_match_three(text):
    pattern = r'a{1}b{3}'
    if re.search(pattern, text, re.IGNORECASE):
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_three('ac'), False)

if __name__ == '__main__':
    unittest.main()