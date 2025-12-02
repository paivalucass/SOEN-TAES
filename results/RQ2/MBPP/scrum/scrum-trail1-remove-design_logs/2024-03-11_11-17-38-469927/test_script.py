def text_match_three(text):
    return 'abb' in text

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(text_match_three('abb'))
        self.assertFalse(text_match_three('ac'))

if __name__ == '__main__':
    unittest.main()