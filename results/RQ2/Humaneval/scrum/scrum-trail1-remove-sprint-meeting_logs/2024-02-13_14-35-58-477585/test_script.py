def split_words(txt):
    import re
    if not isinstance(txt, str) or len(txt) == 0:
        return "Error: Empty string input"

    if ' ' in txt:
        return txt.split()
    elif ',' in txt:
        return txt.split(',')
    else:
        odd_letters_count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return odd_letters_count
import unittest

class Test(unittest.TestCase):
    def test_space_in_txt(self):
        self.assertEqual(split_words('Hello world!'), ["Hello", "world!"])

    def test_comma_in_txt(self):
        self.assertEqual(split_words('Hello,world!'), ["Hello", "world!"])

    def test_no_space_or_comma_in_txt(self):
        self.assertEqual(split_words('abcdef'), 3)

if __name__ == '__main__':
    unittest.main()