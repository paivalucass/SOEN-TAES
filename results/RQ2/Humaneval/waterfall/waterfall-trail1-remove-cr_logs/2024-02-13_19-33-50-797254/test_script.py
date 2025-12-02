import math

# Function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, math.isqrt(num) + 1, 2):
        if num % i == 0:
            return False
    return True

# Function to find the n-th number that is a Fibonacci number and prime

def prime_fib(n: int) -> int:
    fib_cache = {0: 0, 1: 1}
    a, b = 1, 1
    for i in range(2, n + 1):
        fib_num = a + b
        fib_cache[i] = fib_num
        a, b = b, fib_num
    if n in fib_cache:
        num = fib_cache[n]
        if is_prime(num):
            return num
    return None

import unittest

class Test(unittest.TestCase):
    def test_prime_fib(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()