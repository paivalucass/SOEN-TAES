import re
def text_match_three(text):
    pattern = r'a{1}b{3}'
    if re.search(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three('abb'))
        self.assertFalse(text_match_three('ac'))

if __name__ == '__main__':
    unittest.main()