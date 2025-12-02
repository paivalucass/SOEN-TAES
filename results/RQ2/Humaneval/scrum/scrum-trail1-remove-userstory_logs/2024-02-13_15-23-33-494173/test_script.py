def split_words(txt):
    import re
    if not isinstance(txt, str) or not txt:
        return "Invalid input: Please provide a valid non-empty string."

    if re.search(r'\s', txt):
        return re.split(r'\s', txt)
    elif re.search(r',', txt):
        return re.split(r',', txt)
    else:
        count = 0
        for char in txt:
            if char.islower() and ord(char) % 2 != 0:
                count += 1
        return count
import unittest

class Test(unittest.TestCase):
    def test_space(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])

    def test_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])

    def test_no_whitespace_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()