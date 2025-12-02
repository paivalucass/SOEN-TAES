def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(101), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(13441), True)
        self.assertEqual(is_prime(61), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(1), False)

if __name__ == '__main__':
    unittest.main()