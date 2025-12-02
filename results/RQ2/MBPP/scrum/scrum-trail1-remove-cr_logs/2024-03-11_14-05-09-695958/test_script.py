def text_match_three(text):
    if 'abbb' in text:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three("ac"))

if __name__ == '__main__':
    unittest.main()