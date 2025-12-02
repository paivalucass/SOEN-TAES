def find_adverb_position(text):
    '''Write a function to find the first adverb and their positions in a given sentence.'''
    words = text.split()
    adverb = None
    position = None
    for i, word in enumerate(words):
        if word.endswith('ly'):
            adverb = word
            position = (text.index(word), text.index(word) + len(word) - 1, adverb)
            break
    return position
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position('clearly!! we can see the sky'), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()