def geometric_sum(n):
    if not isinstance(n, (int, float)) or n <= 0:
        return "Error: n must be a positive integer"
    elif n == 1:
        return 1.0
    else:
        return 1.0 + 1.0 / geometric_sum(n-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()