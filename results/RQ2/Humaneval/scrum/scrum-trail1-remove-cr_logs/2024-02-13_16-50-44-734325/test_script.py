def is_prime(n):
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
    def test_is_prime(self):
        self.assertEqual(is_prime(6), False)
        self.assertEqual(is_prime(101), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(13441), True)
        self.assertEqual(is_prime(61), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(1), False)

if __name__ == '__main__':
    unittest.main()