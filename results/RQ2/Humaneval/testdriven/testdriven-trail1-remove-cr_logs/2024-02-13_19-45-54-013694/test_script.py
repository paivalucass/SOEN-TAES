def largest_prime_factor(n: int) -> int:
    # Input validation
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    elif is_prime(n):
        raise ValueError("Input must not be a prime number")
    
    # Find largest prime factor
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

# Helper function to check if a number is prime
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
import unittest

class Test(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()