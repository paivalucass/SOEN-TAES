import re

def capital_words_spaces(str1):
    pattern = r'\b[A-Z][a-z]*'
    modified_string = re.sub(pattern, r' \g<0>', str1)
    return modified_string
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(capital_words_spaces('Python'), 'Python')

if __name__ == '__main__':
    unittest.main()