import math

def count_binary_seq(n):
    if not isinstance(n, int) or n < 0 or n > 70:
        raise ValueError
    return math.comb(2*n, n) / (n + 1)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(count_binary_seq(1), 2.0, delta=0.001)

if __name__ == '__main__':
    unittest.main()