def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if not isinstance(a, int) or a < 0 or a >= 100:
        raise ValueError("Input must be a non-negative integer less than 100")

    if a < 6:
        return False

    primes = [2, 3, 5]
    for prime in primes:
        if a % prime == 0:
            if a / prime in primes:
                return True
    return False

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_multiply_prime(30), True)

if __name__ == '__main__':
    unittest.main()