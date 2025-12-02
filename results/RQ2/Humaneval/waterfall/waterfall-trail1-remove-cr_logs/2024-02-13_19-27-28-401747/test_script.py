def split_words(txt):
    if not txt:
        return "Error: Empty input"

    if any(char in txt for char in '!@#$%^&*()_+=-'):
        return "Error: Input contains special characters"
    words = txt.split()
    if len(words) > 1:
        return words
    else:
        comma_split = txt.split(',')
        if len(comma_split) > 1:
            return [word.strip() for word in comma_split]
        else:
            odd_letters_count = sum(1 for char in txt if char.islower() and ord(char) % 2 != 0)
            return odd_letters_count
import unittest

class Test(unittest.TestCase):
    def test_space_split(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma_split(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_letter_count(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()