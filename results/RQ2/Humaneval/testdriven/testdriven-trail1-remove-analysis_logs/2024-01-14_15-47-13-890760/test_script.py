def is_prime(num: int) -> bool:
    """
    Checks if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """
    Returns the n-th Fibonacci number.
    """
    fib_cache = {}
    fib_cache[0] = 0
    fib_cache[1] = 1
    for i in range(2, n + 1):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
    return fib_cache[n]

def prime_fib(n: int) -> int:
    """
    Returns the n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        return None
    count = 0
    i = 0
    while count < n:
        number = fibonacci(i)
        if is_prime(number):
            count += 1
        i += 1
    return number
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