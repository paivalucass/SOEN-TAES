def text_match_three(text):
    return True if 'abbb' in text else False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three("abbb"))
        self.assertFalse(text_match_three("ac"))
        self.assertFalse(text_match_three("abbbb"))
        self.assertTrue(text_match_three("xyzabbb"))

if __name__ == '__main__':
    unittest.main()