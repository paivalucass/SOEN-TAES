def text_match_three(text):
    if len(text) < 4:
        return False
    else:
        text_lower = text.lower()
        if 'a' in text_lower and text_lower.count('b') >= 3:
            return True
        else:
            return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three('abbbc'))
        self.assertFalse(text_match_three('ac'))

if __name__ == '__main__':
    unittest.main()