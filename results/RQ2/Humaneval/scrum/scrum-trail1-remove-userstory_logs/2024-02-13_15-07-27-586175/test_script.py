import re

def remove_vowels(text):
    # Create a regular expression pattern to match all vowels (a, e, i, o, u) in the input string.
    pattern = r'[aeiouAEIOU]'
    
    # Use the re.sub() function to replace all matched vowels with an empty string.
    modified_text = re.sub(pattern, '', text)
    
    # Return the modified string without vowels.
    return modified_text
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_remove_vowels_with_newline(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_remove_all_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_remove_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()