def word_len(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    return len(s) % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()