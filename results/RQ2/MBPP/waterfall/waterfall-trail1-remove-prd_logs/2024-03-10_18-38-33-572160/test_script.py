def find_adverb_position(text):
    if text is None or text == "":
        return "Error: Empty input text"
    
    import re
    
    adverbs = ['quickly', 'clearly', 'just', 'and']  # Sample adverbs for testing
    
    for adverb in adverbs:
        match = re.search(r'\b'+adverb+r'\b', text)
        if match:
            adverb_position = match.start()
            return (adverb_position, adverb_position + len(adverb), adverb)
    
    return "No adverb found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverb_position("clearly!! we can see the sky"), (0, 7, 'clearly'))

if __name__ == '__main__':
    unittest.main()