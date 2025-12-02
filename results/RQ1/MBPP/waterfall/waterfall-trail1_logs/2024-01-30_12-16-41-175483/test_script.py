def find_char_long(text):
    words = text.split()
    result = [word for word in words if len(word) >= 4]
    return result
import unittest

class Test(unittest.TestCase):
    def test_find_char_long(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()