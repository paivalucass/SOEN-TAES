def geometric_sum(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n should be a non-negative integer")

    if n == 0:
        return 1
    else:
        return 1 / (2 ** n) + geometric_sum(n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()