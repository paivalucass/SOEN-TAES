def find_max(words):
    max_unique_chars = 0
    max_unique_word = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_chars:
            max_unique_word = min(max_unique_word, word)
    return max_unique_word
import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()