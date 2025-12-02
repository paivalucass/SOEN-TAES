def select_words(s, n):
    if not s or n <= 0:
        return []

    words = s.split()
    result = []
    vowels = "aeiouAEIOU"

    for word in words:
        consonant_count = sum(1 for letter in word if letter.isalpha() and letter not in vowels)
        if consonant_count == n:
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