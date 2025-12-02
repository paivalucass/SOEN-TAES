def even_binomial_Coeff_Sum(n):
    sum_even_index_binomial_coefficients = 0
    for i in range(n+1):
        coefficient = 1
        for j in range(i+1):
            if j == 0 or j == i:
                coefficient *= 1
            else:
                coefficient = coefficient * (i - j + 1) // j
        if i % 2 == 0:
            sum_even_index_binomial_coefficients += coefficient
    return sum_even_index_binomial_coefficients
import unittest

class Test(unittest.TestCase):
    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()