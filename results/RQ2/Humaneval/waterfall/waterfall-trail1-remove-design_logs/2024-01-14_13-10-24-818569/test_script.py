def largest_prime_factor(n: int) -> int:
    current_prime_factor = 2
    while current_prime_factor * current_prime_factor <= n:
        if n % current_prime_factor != 0:
            current_prime_factor += 1
        else:
            n //= current_prime_factor
    return n

import unittest

class Test(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()