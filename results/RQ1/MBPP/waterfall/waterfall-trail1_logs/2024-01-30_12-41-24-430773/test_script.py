def frequency(a, x):
    if isinstance(x, list):
        count = x.count(a)
        return count
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()