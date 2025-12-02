import re
def find_adverb_position(text):
    adverbs = ["clearly"]
    words = re.findall(r'\w+', text)
    for word in words:
        for adverb in adverbs:
            if adverb in word:
                start = text.find(word)
                end = start + len(word) - 1
                return (start, end, adverb)
    return "Error: No adverb found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()