from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    factors = []
    if n == 1:
        return [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_factorize_8(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_factorize_25(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_factorize_70(self):
        self.assertEqual(factorize(70), [2, 5, 7])

if __name__ == '__main__':
    unittest.main()