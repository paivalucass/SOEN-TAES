def frequency(a, x):
    if not isinstance(a, list) or not isinstance(x, (int, float)):
        raise TypeError("Input parameters are not of the correct type")

    if not a:
        return 0
    if x not in a:
        return 0
    else:
        return a.count(x)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()