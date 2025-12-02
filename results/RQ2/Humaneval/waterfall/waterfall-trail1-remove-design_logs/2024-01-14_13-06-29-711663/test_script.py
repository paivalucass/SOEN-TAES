from typing import List

def factorize(n: int) -> List[int]:
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"

    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
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