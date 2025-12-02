def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    import re
    return re.sub(r'[aeiouAEIOU]', '', text)
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')
        
    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')
        
    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')
        
    def test_string_with_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')
        
    def test_mixed_case_vowels(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

if __name__ == '__main__':
    unittest.main()