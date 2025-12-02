def split_words(txt):
    if isinstance(txt, str):
        if ' ' in txt:
            return txt.split()
        elif ',' in txt:
            return txt.split(',')
        else:
            odd_count = len([letter for letter in txt if letter.islower() and ord(letter) % 2 != 0])
            return odd_count
    else:
        return "Error: Input is not a string" if txt else "Error: Empty input string"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()