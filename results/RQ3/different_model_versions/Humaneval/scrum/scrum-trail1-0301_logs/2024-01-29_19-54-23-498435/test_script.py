def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    :param text: The input string containing vowels to be removed
    :type text: str
    :return: The input string without vowels
    :rtype: str
    """
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result
import unittest


class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

    def test_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_multiple_lines(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_single_line(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')


if __name__ == '__main__':
    unittest.main()