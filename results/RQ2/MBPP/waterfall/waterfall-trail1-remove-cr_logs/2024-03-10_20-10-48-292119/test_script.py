from math import comb

def sum_of_product(n):
    product_sum = 0
    for k in range(n-1):
        product_sum += comb(n, k) * comb(n, k+1)
    return product_sum

# Example usage
assert sum_of_product(3) == 15
import unittest

class Test(unittest.TestCase):
    def test_binomial_Coeff(self):
        self.assertEqual(binomial_Coeff(3, 2), 3)  # Example input and output

if __name__ == '__main__':
    unittest.main()