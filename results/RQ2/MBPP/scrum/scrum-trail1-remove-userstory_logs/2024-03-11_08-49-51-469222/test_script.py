def find_char_long(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')

    words = text.split()

    long_words = {word for word in words if len(word) >= 4}

    return long_words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()