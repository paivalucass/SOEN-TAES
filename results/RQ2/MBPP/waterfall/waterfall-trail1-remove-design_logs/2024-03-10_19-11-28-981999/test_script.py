def even_binomial_Coeff_Sum(n):
    import math

    sum_of_even_coefficients = 0
    for i in range(n + 1):
        if i % 2 == 0:
            sum_of_even_coefficients += math.comb(n, i)

    return sum_of_even_coefficients
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()