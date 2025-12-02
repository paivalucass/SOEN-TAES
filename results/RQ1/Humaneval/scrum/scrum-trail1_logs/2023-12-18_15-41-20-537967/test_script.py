def select_words(s, n):
    if not isinstance(s, str) or not isinstance(n, int) or n <= 0:
        return "Invalid input"

    def count_consonants(word):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        return sum(1 for letter in word if letter in consonants)

    words = s.split()
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result
import unittest

class Test(unittest.TestCase):
    def test_select_words(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()