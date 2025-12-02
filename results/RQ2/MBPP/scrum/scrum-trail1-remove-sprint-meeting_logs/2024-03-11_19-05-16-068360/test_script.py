def geometric_sum(n):
    if n == 0:
        return 1
    else:
        return 1 / (2 ** (n-1)) + geometric_sum(n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()