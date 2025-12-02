def find_max(words):
    if not words:
        return "Error: Input list is empty"

    for word in words:
        if not isinstance(word, str):
            return "Error: Input list contains non-string elements"

    max_word = ""
    max_unique_chars = 0
    for word in words:
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        unique_chars = len(char_count)
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word
    return max_word
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()