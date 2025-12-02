def even_binomial_Coeff_Sum(n):
    def calculate_binomial_coefficient(n, k):
        if k > n - k:
            k = n - k
        res = 1
        for i in range(k):
            res *= (n - i)
            res //= (i + 1)
        return res
    sum_even = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum_even += calculate_binomial_coefficient(n, i)
    return sum_even
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_binomial_Coeff_Sum(4), 8)

if __name__ == '__main__':
    unittest.main()