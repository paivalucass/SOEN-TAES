import re

def find_adverb_position(text):
    adverb_match = re.search(r'\b\w+ly\b', text)
    if adverb_match:
        return adverb_match.start(), adverb_match.end(), adverb_match.group()
    else:
        return None
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position('clearly!! we can see the sky'), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()