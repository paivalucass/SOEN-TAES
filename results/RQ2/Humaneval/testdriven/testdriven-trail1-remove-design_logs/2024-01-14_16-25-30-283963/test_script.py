def select_words(s, n):
    if not isinstance(n, int) or not isinstance(s, str):
        raise ValueError("Invalid input. 'n' should be a natural number and 's' should be a string.")

    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for letter in word if letter in consonants)

    if not s:
        return []

    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
    return result

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])

    def test2(self):
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])

    def test3(self):
        self.assertEqual(select_words("simple white space", 2), [])

    def test4(self):
        self.assertEqual(select_words("Hello world", 4), ["world"])

    def test5(self):
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

    def test6(self):
        self.assertEqual(select_words("", 2), [])

if __name__ == '__main__':
    unittest.main()