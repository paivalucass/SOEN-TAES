def count_binary_seq(n):
    if n <= 0:
        return 0.0
    elif n == 1:
        return 2.0
    else:
        return 2 * (2 * n - 1) * count_binary_seq(n - 1)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_binary_seq(1), 2.0)

if __name__ == '__main__':
    unittest.main()