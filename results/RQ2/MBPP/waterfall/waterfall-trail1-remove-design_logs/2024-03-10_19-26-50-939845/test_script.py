def text_match_three(text):
    import re
    pattern = r'ab{3}\w*'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three('abbb'))
        self.assertFalse(text_match_three('ac'))
        self.assertFalse(text_match_three('abb'))
        self.assertFalse(text_match_three('ab'))

if __name__ == '__main__':
    unittest.main()