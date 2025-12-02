def find_adverbs(text):
    adverb_positions = []
    words = text.split()
    for i in range(len(words)):
        if words[i].endswith('ly'):
            adverb_positions.append(str(i) + '-' + str(i + len(words[i]) - 1) + ': ' + words[i])
    return adverb_positions[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()