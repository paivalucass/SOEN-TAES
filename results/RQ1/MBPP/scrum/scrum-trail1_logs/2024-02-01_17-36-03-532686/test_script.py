def find_adverbs(text):
    words = text.split()
    adverbs = [(i, word) for i, word in enumerate(words) if word.endswith('ly')]
    if adverbs:
        position, adverb = adverbs[0]
        return f'{position}-{position + len(adverb) - 1}: {adverb}'
    else:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs('Clearly, he has no excuse for such behavior.'), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()