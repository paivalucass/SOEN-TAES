def largest_prime_factor(n: int) -> int:
    if n <= 1:
        return None
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n if n > 1 else factor
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()