def extract_rear(test_tuple):
    if not isinstance(test_tuple, tuple):
        return "Error: Input is not a tuple"
    if not all(isinstance(word, str) for word in test_tuple):
        return "Error: Input is not a tuple of strings"
    if len(test_tuple) == 0:
        return "Error: Input tuple is empty"
    
    return [word[-1] for word in test_tuple]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_rear(('Mers', 'for', 'Vers')), ['s', 'r', 's'])

if __name__ == '__main__':
    unittest.main()