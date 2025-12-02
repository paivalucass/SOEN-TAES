def remove_vowels(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a valid string")
    
    result = ''.join([char for char in text if char.lower() not in ['a', 'e', 'i', 'o', 'u']])
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_multiple_words(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_single_word(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_all_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()