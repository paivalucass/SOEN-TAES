def find_adverbs(text):
    import re
    adverbs = [(m.group(0), m.start(), m.end()) for m in re.finditer(r'\b\w+ly\b', text)]
    if adverbs:
        return f"{adverbs[0][1]}-{adverbs[0][2]}: {adverbs[0][0]}"
    else:
        return "No adverbs found"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()