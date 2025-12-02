from typing import List

def select_words(s: str, n: int) -> List[str]:
    import re

    if not re.match("^[a-zA-Z\\s]*$", s):
        return []

    if not s:
        return []

    def is_consonant(c):
        return c.lower() not in "aeiou"

    def count_consonants(word):
        return sum(1 for letter in word if is_consonant(letter))

    words = s.split()
    result = [word for word in words if count_consonants(word) == n]
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