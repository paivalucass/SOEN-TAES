def find_adverbs(text):
    adverbs = [(i, i + 1 + len(word)) for i, word in enumerate(text.split()) if word.endswith('ly')]
    if adverbs:
        return f'{adverbs[0][0]}-{adverbs[0][1]}: {text[adverbs[0][0]:adverbs[0][1]]}'
    else:
        return ''
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), "0-7: Clearly")

if __name__ == '__main__':
    unittest.main()