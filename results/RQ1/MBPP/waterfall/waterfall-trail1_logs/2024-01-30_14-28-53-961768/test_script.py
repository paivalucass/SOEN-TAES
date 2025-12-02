import re

def find_adverb_position(text):
    adverbs = ["clearly", "quickly", "slowly", "elegantly", "happily"]  # Add more adverbs as needed
    words = re.findall(r'\b\w+\b', text)

    for word in adverbs:
        if word in words:
            start_position = text.find(word)
            return (words.index(word), start_position, word)

    raise ValueError("No adverb found in input data")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position('clearly!! we can see the sky'), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()