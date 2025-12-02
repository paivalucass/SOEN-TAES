def binomial_Coeff(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < k:
        return "Invalid input"
    
    result = 1
    for i in range(1, k + 1):
        result *= (n - i + 1)
        result //= i
    return result

def product_Of_binomial_Coefficients(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < k:
        return "Invalid input"

    product = binomial_Coeff(n, k) * binomial_Coeff(n, k+1)
    return product

def sum_Of_product(n, k):
    if not isinstance(n, int) or not isinstance(k, int) or n < k:
        return "Invalid input"

    sum_result = product_Of_binomial_Coefficients(n, k) + product_Of_binomial_Coefficients(n, k+1)
    return sum_result
import unittest

class Test(unittest.TestCase):
    def test_binomial_Coeff(self):
        self.assertEqual(binomial_Coeff(3, 2), 3)
        self.assertEqual(binomial_Coeff(4, 2), 6)

if __name__ == '__main__':
    unittest.main()