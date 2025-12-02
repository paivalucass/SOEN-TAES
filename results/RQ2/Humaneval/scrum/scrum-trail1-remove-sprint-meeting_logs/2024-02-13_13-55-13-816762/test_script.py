import re

def remove_vowels(text):
    result = re.sub(r'[aeiouAEIOU]', '', text)
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_newline(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_with_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()