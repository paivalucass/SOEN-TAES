def is_bored(S):
    if not S:
        return 0
    
    boredoms = 0
    sentences = S.split(".")
    for sentence in sentences:
        if sentence.strip() and sentence.strip()[0] == "I":
            boredoms += 1
    
    return boredoms
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored('Hello world'), 0)
        self.assertEqual(is_bored('The sky is blue. The sun is shining. I love this weather'), 1)

if __name__ == '__main__':
    unittest.main()