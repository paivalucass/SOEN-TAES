from typing import List

def factorize(n: int) -> List[int]:
    if n <= 1:
        return []

    prime_factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            prime_factors.append(divisor)
            n //= divisor
        divisor += 1

    return prime_factors
import unittest
from typing import List

class Test(unittest.TestCase):
    def test_factorize(self):
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])

if __name__ == '__main__':
    unittest.main()