def largest_prime_factor(n: int) -> int:
    if n < 2:
        return None  # or raise an exception
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
        else:
            p += 1
    return n
import unittest

class Test(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()