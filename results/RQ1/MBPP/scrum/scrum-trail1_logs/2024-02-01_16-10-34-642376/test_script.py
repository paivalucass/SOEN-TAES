def find_adverbs(text):
    words = text.split()
    adverb = ''
    for i, word in enumerate(words):
        if word.endswith('ly'):
            adverb = f'{i}-{i + 1}: {word}'
            break
    return adverb
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs('Clearly, he has no excuse for such behavior.'), '0-1: Clearly')

if __name__ == '__main__':
    unittest.main()