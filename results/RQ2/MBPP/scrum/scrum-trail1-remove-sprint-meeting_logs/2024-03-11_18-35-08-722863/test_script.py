import re

def text_match_two_three(text):
    pattern = 'ab{2,3}'
    return bool(re.search(pattern, text))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_two_three('ac'), False)

if __name__ == '__main__':
    unittest.main()