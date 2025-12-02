from typing import List

def factorize(n: int) -> List[int]:
    if n <= 0:
        raise ValueError("Input number must be positive")
    
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors
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