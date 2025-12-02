def remove_vowels(text):
    import re
    if not isinstance(text, str):
        return None
    return re.sub(r'[aeiouAEIOU]', '', text)
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_multiple_lines(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_single_line(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()