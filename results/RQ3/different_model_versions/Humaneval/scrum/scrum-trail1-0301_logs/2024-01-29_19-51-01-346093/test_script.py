def is_prime(n):
    """
    Return True if a given number is prime, and False otherwise.

    """
    if not isinstance(n, int) or n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
import unittest

class TestPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()