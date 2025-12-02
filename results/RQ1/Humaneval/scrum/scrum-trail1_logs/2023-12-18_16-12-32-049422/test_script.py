from typing import List

def factorize(n: int) -> List[int]:
    """
    Return a list of prime factors of the given integer in the order from smallest to largest.
    Each prime factor will be listed the number of times it appears in the factorization.
    The input number will be equal to the product of all factors.
    """
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        divisor += 1
    return factors
import unittest

class Test(unittest.TestCase):
    def test_factorize_8(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_factorize_25(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_factorize_70(self):
        self.assertEqual(factorize(70), [2, 5, 7])

if __name__ == '__main__':
    unittest.main()