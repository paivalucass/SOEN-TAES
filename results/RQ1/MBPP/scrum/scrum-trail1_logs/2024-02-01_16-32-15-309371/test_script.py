def text_match_wordz_middle(text):
    words = text.split()
    middle_word_index = len(words) // 2
    middle_word = words[middle_word_index]

    # Check if 'z' is in the middle word, excluding the start and end of the word
    if 'z' in middle_word[1:-1]:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(text_match_wordz_middle('pythonzabc.'), True)

if __name__ == '__main__':
    unittest.main()