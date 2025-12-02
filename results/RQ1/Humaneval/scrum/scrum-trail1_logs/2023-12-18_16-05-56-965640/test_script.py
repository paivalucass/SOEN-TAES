def find_max(words):
    if not words:
        return "Input list is empty"

    max_word = ""
    max_unique_chars = 0
    char_count = {}

    for word in words:
        unique_chars = len(set(word))
        
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word
            
    return max_word
import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb", "cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()