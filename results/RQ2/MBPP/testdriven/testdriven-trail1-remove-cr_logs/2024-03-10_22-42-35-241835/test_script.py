# Function to match a word containing the letter 'z'
import re

def text_match_wordz(text):
    # Use regular expressions to match the letter 'z' in the input text
    if re.search(r'\b\w*z\w*\b', text):
        return True
    else:
        return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz('pythonz.'), True)

if __name__ == '__main__':
    unittest.main()