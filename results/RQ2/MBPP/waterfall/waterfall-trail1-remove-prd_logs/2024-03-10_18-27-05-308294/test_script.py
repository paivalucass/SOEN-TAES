def word_len(s):
    if not isinstance(s, str):
        raise ValueError("Input parameter is not a string")
    length = len(s)
    return length % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()