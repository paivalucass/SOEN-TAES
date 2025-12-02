import re
def text_match_wordz_middle(text):
    '''This function checks if a string contains 'z' in the middle of each word.'''
    # Input validation
    if not isinstance(text, str):
        return "Input is not a string"

    # Using regular expression to efficiently check for 'z' in the middle of each word
    pattern = r'\b\w+z\w*\b'
    match = re.search(pattern, text)

    if match:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle("pythonzabc."), True)

if __name__ == '__main__':
    unittest.main()