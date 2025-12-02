def find_max(words):
    """
    Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """

    # Initialize variables for max unique character count and word
    max_unique_char_count = 0
    max_unique_char_word = ""

    # Iterate through the list of words
    for word in words:
        # Calculate the number of unique characters in the word
        unique_char_count = len(set(word))
        
        # Check if the current word has more unique characters than the previous max
        if unique_char_count > max_unique_char_count:
            max_unique_char_count = unique_char_count
            max_unique_char_word = word
        # If the current word has the same number of unique characters as the previous max
        # Check lexicographical order and update max_unique_char_word accordingly
        elif unique_char_count == max_unique_char_count:
            max_unique_char_word = min(max_unique_char_word, word)

    return max_unique_char_word
import unittest

class Test(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max(["name", "of", "string"]), "string")
        self.assertEqual(find_max(["name", "enam", "game"]), "enam")
        self.assertEqual(find_max(["aaaaaaa", "bb" ,"cc"]), "aaaaaaa")

if __name__ == '__main__':
    unittest.main()