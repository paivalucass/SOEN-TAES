import re

def find_adverbs(text):
    if text is None or text == "":
        return "Input text is empty or None"
    
    words = re.findall(r'\b\w+ly\b', text)
    if words:
        adverb = words[0]
        start = text.find(adverb)
        end = start + len(adverb)
        return f"{start}-{end}: {adverb}"
    return "No adverbs ending with ly found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-1: Clearly')

if __name__ == '__main__':
    unittest.main()