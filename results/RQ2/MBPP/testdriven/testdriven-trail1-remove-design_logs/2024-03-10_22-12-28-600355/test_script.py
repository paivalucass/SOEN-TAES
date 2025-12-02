def find_adverbs(text):
    adverbs = [word for word in text.split() if word.endswith('ly')]
    if adverbs:
        first_adverb = adverbs[0]
        start_index = text.find(first_adverb)
        end_index = start_index + len(first_adverb) - 1
        return f"{start_index}-{end_index}: {first_adverb}"
    else:
        return None
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs('Clearly, he has no excuse for such behavior.'), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()