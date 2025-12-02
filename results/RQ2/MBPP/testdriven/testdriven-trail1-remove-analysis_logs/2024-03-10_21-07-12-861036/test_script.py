def find_char_long(text):
    '''
    Write a function to find all words which are at least 4 characters long in a string.
    assert set(find_char_long('Please move back to stream')) == set(['Please', 'move', 'back', 'stream'])
    '''
    # Split the input text into words
    words = text.split()

    # Filter the words that are at least 4 characters long
    long_words = [word for word in words if len(word) >= 4]

    return long_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()