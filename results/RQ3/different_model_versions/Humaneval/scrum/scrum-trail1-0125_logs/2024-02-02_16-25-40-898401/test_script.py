def split_words(txt):
    words = []
    if ' ' in txt:
        words = txt.split()
    elif ',' in txt:
        words = txt.split(',')
    else:
        odd_letters = [c for c in txt if c.islower() and ord(c) % 2 != 0]
        return len(odd_letters)
    return words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()