def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
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