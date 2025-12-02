def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        if sentence:
            words = sentence.split()
            if words[0] == 'I':
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

if __name__ == '__main__':
    unittest.main()