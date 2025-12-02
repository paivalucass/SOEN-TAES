def binomial_Coeff(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_Coeff(n-1, k-1) + binomial_Coeff(n-1, k)

def sum_Of_product(n):
    return binomial_Coeff(n, 1) * binomial_Coeff(n, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(binomial_Coeff(3, 2), 3)  # Example input and output

if __name__ == '__main__':
    unittest.main()