def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    return ''.join([char for char in text if char not in vowels])
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')
        self.assertEqual(remove_vowels('aaaaa'), '')
        self.assertEqual(remove_vowels('aaBAA'), 'B')
    
    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()