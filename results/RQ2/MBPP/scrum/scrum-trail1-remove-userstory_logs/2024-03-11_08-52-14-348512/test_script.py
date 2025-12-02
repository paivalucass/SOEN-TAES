def word_len(s):
    if type(s) != str or len(s) == 0:
        return "Invalid input"
    return len(s) % 2 != 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(word_len('Hadoop'), False)

if __name__ == '__main__':
    unittest.main()