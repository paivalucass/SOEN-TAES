import re

def find_adverbs(text):
    if not isinstance(text, str):
        raise ValueError("Input text must be a string")
    
    adverbs = re.findall(r'\b\w+ly\b', text)
    if adverbs:
        position = text.find(adverbs[0])
        return f"{position}-{position + len(adverbs[0]) - 1}: {adverbs[0]}"
    else:
        raise ValueError("No adverbs ending with 'ly' found in the input text")
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs('Clearly, he has no excuse for such behavior.'), '0-6: Clearly')

if __name__ == '__main__':
    unittest.main()