def geometric_sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    if n == 1:
        return 1.0
    else:
        return 1/n + geometric_sum(n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()