import re

def is_bored(S):
    boredoms = 0
    sentences = re.split('[.!?]', S)
    for sentence in sentences:
        if sentence.strip().startswith('I '):
            boredoms += 1
    return boredoms
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored('Hello world'), 0)
        self.assertEqual(is_bored('The sky is blue. The sun is shining. I love this weather'), 1)

if __name__ == '__main__':
    unittest.main()