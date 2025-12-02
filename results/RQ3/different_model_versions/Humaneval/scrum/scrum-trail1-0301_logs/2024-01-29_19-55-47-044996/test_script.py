def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.
    Return None for negative input values, non-integer input values, 1, and 0.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if not isinstance(n, int) or n < 2:
        return None
    
    if n == 2:
        return 2
    
    while n % 2 == 0:
        n //= 2
    
    if n == 1:
        return 2
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 2
    
    return n
import unittest

class Test(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()