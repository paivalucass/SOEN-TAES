def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1)

if __name__ == '__main__':
    unittest.main()