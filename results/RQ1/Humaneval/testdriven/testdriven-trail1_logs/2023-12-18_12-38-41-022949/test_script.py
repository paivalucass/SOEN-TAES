def split_words(txt):
    import re
    if not txt:
        return []

    if re.search(r'\s', txt):
        return re.split(r'\s', txt)
    elif re.search(r',', txt):
        return re.split(r',', txt)
    else:
        count = sum(1 for c in txt if c.islower() and ord(c) % 2 != 0)
        return count
import unittest

class Test(unittest.TestCase):
    def test_space(self):
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
    
    def test_comma(self):
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
    
    def test_no_space_or_comma(self):
        self.assertEqual(split_words("abcdef"), 3)

if __name__ == '__main__':
    unittest.main()