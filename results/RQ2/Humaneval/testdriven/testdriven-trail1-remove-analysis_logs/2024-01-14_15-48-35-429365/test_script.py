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
    if text is None or text == "":
        return ""
    result = "".join([char for char in text if char.lower() not in ['a', 'e', 'i', 'o', 'u']])
    return result
import unittest

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_without_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()