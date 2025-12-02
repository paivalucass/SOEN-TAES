def find_adverbs(text):
    import re
    
    adverbs = re.finditer(r'\b\w+ly\b', text)
    result = ""
    for adverb in adverbs:
        result += f"{adverb.start()}-{adverb.end()}: {adverb.group()}"
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()