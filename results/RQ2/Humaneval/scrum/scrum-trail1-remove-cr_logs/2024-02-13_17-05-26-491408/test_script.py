def is_bored(S):
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if len(words) > 0 and words[0] == 'I':
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

if __name__ == '__main__':
    unittest.main()