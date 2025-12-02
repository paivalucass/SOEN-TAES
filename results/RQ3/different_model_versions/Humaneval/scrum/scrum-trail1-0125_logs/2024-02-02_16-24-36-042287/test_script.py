def select_words(s, n):
    vowels = 'aeiouAEIOU'
    words = s.split()
    result = []
    for word in words:
        consonants_count = sum(1 for letter in word if letter.isalpha() and letter not in vowels)
        if consonants_count == n:
            result.append(word)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(select_words("Mary had a little lamb", 4), ["little"])
        self.assertEqual(select_words("Mary had a little lamb", 3), ["Mary", "lamb"])
        self.assertEqual(select_words("simple white space", 2), [])
        self.assertEqual(select_words("Hello world", 4), ["world"])
        self.assertEqual(select_words("Uncle sam", 3), ["Uncle"])

if __name__ == '__main__':
    unittest.main()