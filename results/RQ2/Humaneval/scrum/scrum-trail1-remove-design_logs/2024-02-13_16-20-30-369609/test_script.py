def select_words(s, n):
    words = s.split()
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    result = [word for word in words if sum(1 for c in word if c in consonants) == n]
    return result
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test_2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test_3(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test_4(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test_5(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()