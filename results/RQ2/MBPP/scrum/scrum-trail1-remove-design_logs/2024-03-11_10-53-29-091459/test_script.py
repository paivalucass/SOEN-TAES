def find_adverbs(text):
    words = text.split()
    for idx, word in enumerate(words):
        if word.endswith('ly'):
            return f'{idx}-{idx + len(word)}: {word}'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-6: Clearly')

if __name__ == '__main__':
    unittest.main()