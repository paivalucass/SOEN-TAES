import re

def is_pattern_present(text):
    pattern = r'ab+'
    return bool(re.search(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_zero_one('ac'), False)

if __name__ == '__main__':
    unittest.main()