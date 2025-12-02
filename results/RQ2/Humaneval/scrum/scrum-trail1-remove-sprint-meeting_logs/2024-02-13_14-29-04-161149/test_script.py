def find_max(words):
    if not isinstance(words, list) or not all(isinstance(word, str) for word in words):
        return "Invalid input: Please provide a list of strings."

    max_unique_count = 0
    max_unique_word = ""

    for word in words:
        unique_characters = len(set(word))
        if unique_characters > max_unique_count:
            max_unique_count = unique_characters
            max_unique_word = word
        elif unique_characters == max_unique_count:
            max_unique_word = min(word, max_unique_word)

    return max_unique_word
import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()