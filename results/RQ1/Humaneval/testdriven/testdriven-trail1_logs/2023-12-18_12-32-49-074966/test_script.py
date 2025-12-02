import re

def is_bored(S):
    def split_sentences(input_string):
        return re.split('[.!?]', input_string)

    def count_i_starting_sentences(sentences):
        return sum(1 for sentence in sentences if sentence.strip().startswith('I'))

    def validate_input(input_string):
        return isinstance(input_string, str) and len(input_string) > 0

    if validate_input(S):
        sentences = split_sentences(S)
        return count_i_starting_sentences(sentences)
    else:
        return 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_bored('Hello world'), 0)
        self.assertEqual(is_bored('The sky is blue. The sun is shining. I love this weather'), 1)

if __name__ == '__main__':
    unittest.main()