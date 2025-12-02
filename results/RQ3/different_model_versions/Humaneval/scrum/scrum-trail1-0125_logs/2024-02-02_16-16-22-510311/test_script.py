def remove_vowels(text):
    vowels = set('aeiouAEIOU')
    output_str = ''.join(char for char in text if char not in vowels)
    return output_str

# Test cases:
print(remove_vowels(""))  # Output: ""
print(remove_vowels("abcdef\nghijklm"))  # Output: "bcdf\nghjklm"
print(remove_vowels("abcdef"))  # Output: "bcdf"
print(remove_vowels("aaaaa"))  # Output: ""
print(remove_vowels("aaBAA"))  # Output: "B"
print(remove_vowels("zbcd"))  # Output: "zbcd"
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