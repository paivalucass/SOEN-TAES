def count_X(tup, x):
    return tup.count(x)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()