def find_adverb_position(text):
    if not isinstance(text, str):
        return "Invalid input: not a string"

    words = text.split()

    for i, word in enumerate(words):
        word = word.rstrip('!')
        if word.endswith("ly"):
            return (text.find(word), i, word)

    return "No adverb found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()