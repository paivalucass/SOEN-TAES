import math

def binomial_Coeff(n, k):
    result = 0
    for i in range(0, k+1):
        result += math.comb(n, i) * math.comb(n, k-i)
    return result
import unittest

class Test(unittest.TestCase):
    def test_sum_Of_product(self):
        self.assertEqual(binomial_Coeff(3, 2) * binomial_Coeff(3, 1) + binomial_Coeff(3, 1) * binomial_Coeff(3, 0), 15)

if __name__ == '__main__':
    unittest.main()