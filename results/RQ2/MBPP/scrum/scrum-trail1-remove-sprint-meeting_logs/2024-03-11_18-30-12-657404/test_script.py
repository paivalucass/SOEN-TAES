def count_X(tup, x):
    if not isinstance(tup, tuple):
        raise TypeError("Input 'tup' must be a tuple")
    if not isinstance(x, (int, float, str)):
        raise TypeError("Input 'x' must be of type int, float, or str")

    if len(tup) == 0:
        return 0
    else:
        return tup.count(x)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4), 0)

if __name__ == '__main__':
    unittest.main()