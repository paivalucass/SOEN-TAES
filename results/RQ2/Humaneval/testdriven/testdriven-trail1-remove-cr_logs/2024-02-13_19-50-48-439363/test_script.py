def select_words(s, n):
    words = s.split()
    result = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in ['a', 'e', 'i', 'o', 'u'] and letter.isalpha():
                consonants += 1
        if consonants == n:
            result.append(word)
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

    def test_6(self):
        self.assertEqual(select_words("", 3), [])

if __name__ == '__main__':
    unittest.main()