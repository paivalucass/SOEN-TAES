def is_bored(S):
    import re
    if not S.strip():
        return "Error: Input string is empty"
    
    pattern = r'^I\s'
    sentences = re.split(r'[.?!]', S)
    boredom_count = sum(1 for sentence in sentences if re.match(pattern, sentence.strip()))
    
    return boredom_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 1)

if __name__ == '__main__':
    unittest.main()