def is_not_prime(n):
    """
    This function checks if a number is not prime.
    """
    if n < 2:
        return True
    if n == 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_not_prime(2), False)

if __name__ == '__main__':
    unittest.main()