def number_of_substrings(s):
    n = len(s)
    return n*(n+1)//2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(number_of_substrings('abc'), 6)

if __name__ == '__main__':
    unittest.main()