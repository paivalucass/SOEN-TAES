import re

def text_match_three(text):
    # Use regular expressions to check for the pattern 'ab{3}' in the input string
    if re.search(r'ab{3}', text):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_text_match_three(self):
        self.assertTrue(text_match_three('ac'))

if __name__ == '__main__':
    unittest.main()