from math import comb

def even_binomial_Coeff_Sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    sum_of_even_binomial_coefficients = sum(comb(n, k) for k in range(0, n+1, 2))

    return sum_of_even_binomial_coefficients
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()