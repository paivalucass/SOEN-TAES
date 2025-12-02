import re

def find_char_long(text):
    '''Write a function to find all words which are at least 4 characters long in a string.'''
    if not isinstance(text, str):
        raise TypeError("Input data should be a string")

    words = re.findall(r'\b\w{4,}\b', text)
    return set(words)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()