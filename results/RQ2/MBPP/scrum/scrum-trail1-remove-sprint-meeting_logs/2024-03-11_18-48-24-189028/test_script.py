def sumofFactors(n):
    import math

    def findFactors(n):
        factors = []
        for i in range(1, int(math.sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return factors

    def filterEvenFactors(factors):
        even_factors = [factor for factor in factors if factor % 2 == 0]
        return even_factors

    def calculateSum(even_factors):
        return sum(even_factors)

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input number must be a positive integer")

    factors = findFactors(n)
    even_factors = filterEvenFactors(factors)

    return calculateSum(even_factors)
import unittest

class Test(unittest.TestCase):
    def test_sumofFactors(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()