import re

def is_bored(S):
    sentences = re.split(r'[.?!]', S)
    boredom_count = 0
    for sentence in sentences:
        if sentence.strip().startswith('I'):
            boredom_count += 1
    return boredom_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

if __name__ == '__main__':
    unittest.main()