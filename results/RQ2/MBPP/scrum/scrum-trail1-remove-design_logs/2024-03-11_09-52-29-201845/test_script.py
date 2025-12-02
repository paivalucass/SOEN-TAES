def find_char_long(text):
    import re
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    words = re.findall(r'\b\w{4,}\b', text)
    return words
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(set(find_char_long('Please move back to stream')), set(['Please', 'move', 'back', 'stream']))

if __name__ == '__main__':
    unittest.main()