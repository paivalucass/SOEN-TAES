def even_binomial_Coeff_Sum(n):
    memo = {}

    def binomialCoefficient(n, k):
        if k == 0 or k == n:
            return 1
        if (n, k) in memo:
            return memo[(n, k)]
        result = binomialCoefficient(n-1, k-1) + binomialCoefficient(n-1, k)
        memo[(n, k)] = result
        return result

    result = 0
    for i in range(n+1):
        if i % 2 == 0:
            result += binomialCoefficient(n, i)
    return result

import unittest

class Test(unittest.TestCase):
    def test_even_binomial_Coeff_Sum(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()