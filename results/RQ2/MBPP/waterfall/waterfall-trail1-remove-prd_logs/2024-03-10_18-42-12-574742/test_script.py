def find_adverbs(text):
    words = text.split()
    adverb_positions = []
    for i, word in enumerate(words):
        if word.endswith("ly"):
            adverb_positions.append(f"{i}-{i + len(word) - 1}: {word}")
    if adverb_positions:
        return "\n".join(adverb_positions)
    else:
        return 'No adverbs found'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()