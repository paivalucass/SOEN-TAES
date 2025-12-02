def find_char_long(text):
    if text is None or not isinstance(text, str):
        raise ValueError("Input must be a non-empty string")

    return [word for word in text.split() if len(word) >= 4]
import unittest

class Test(unittest.TestCase):
    def test_find_char_long(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()