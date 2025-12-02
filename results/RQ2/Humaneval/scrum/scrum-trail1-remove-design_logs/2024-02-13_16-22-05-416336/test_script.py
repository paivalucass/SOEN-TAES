def split_words(txt):
    if not isinstance(txt, str):
        return "Input is not a string"

    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
        return count
import unittest

class Test(unittest.TestCase):
    def test_split_words_with_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_split_words_with_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_split_words_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()