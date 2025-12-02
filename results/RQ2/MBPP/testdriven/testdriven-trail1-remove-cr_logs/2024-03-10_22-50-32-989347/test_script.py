def geometric_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1.0
    else:
        return 1 / pow(2, n-1) + geometric_sum(n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()