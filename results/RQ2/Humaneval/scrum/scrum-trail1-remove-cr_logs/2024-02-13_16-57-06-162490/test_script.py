def remove_vowels(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    result = ""
    for char in text:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += char
    return result
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

    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()