import math

def largest_prime_factor(n: int):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return max(factors)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()