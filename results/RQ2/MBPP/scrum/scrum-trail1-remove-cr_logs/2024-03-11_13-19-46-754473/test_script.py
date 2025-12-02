def find_adverb_position(text):
    '''Write a function to find the first adverb and their positions in a given sentence.'''
    adverbs = [word.strip('!') for word in text.split() if word.endswith('ly')]
    if adverbs:
        adverb = adverbs[0]
        start = text.index(adverb)
        end = start + len(adverb)
        return (start, end, adverb)
    else:
        return None

import re
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position('clearly!! we can see the sky'), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()