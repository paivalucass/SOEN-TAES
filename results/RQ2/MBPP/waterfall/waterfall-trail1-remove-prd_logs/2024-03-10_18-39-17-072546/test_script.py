def sum_of_factors(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input number must be a positive integer")

    def get_factors(num):
        factors = [i for i in range(1, int(num ** 0.5) + 1) if num % i == 0]
        return factors + [num // i for i in factors if i != num // i]

    even_factors_sum = sum(factor for factor in get_factors(n) if factor % 2 == 0)
    return even_factors_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()