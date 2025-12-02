def split_words(txt):
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        words = txt.split(',')
        if len(words) > 1:
            return words
        else:
            count = sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
            return count
import unittest

class Test(unittest.TestCase):
    def test_split_words_with_whitespace(self):
        self.assertEqual(split_words('Hello world!'), ['Hello', 'world!'])

    def test_split_words_with_comma(self):
        self.assertEqual(split_words('Hello,world!'), ['Hello', 'world!'])

    def test_split_words_no_whitespace_or_comma(self):
        self.assertEqual(split_words('abcdef'), 3)

if __name__ == '__main__':
    unittest.main()