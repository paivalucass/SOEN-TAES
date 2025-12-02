def find_max(words):
    max_unique_chars = 0
    word_with_max_unique_chars = ""

    for word in words:
        unique_chars_set = set(word)
        if len(unique_chars_set) > max_unique_chars:
            max_unique_chars = len(unique_chars_set)
            word_with_max_unique_chars = word
        elif len(unique_chars_set) == max_unique_chars:
            word_with_max_unique_chars = min(word, word_with_max_unique_chars)

    return word_with_max_unique_chars

import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()