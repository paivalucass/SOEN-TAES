import math

def count_binary_seq(n):
    def binomial_coef(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return binomial_coef(n-1, k-1) + binomial_coef(n-1, k)

    count = 0
    for i in range(n+1):
        count += binomial_coef(2*n, i)
    return count / (2**n)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(count_binary_seq(1), 2.0, delta=0.001)

if __name__ == '__main__':
    unittest.main()