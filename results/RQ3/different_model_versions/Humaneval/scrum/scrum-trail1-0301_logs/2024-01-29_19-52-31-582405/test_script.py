def prime_fib(n: int):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def fibonacci(num):
        if num <= 1:
            return num
        return fibonacci(num-1) + fibonacci(num-2)
    
    def memoize(func):
        cache = {}
        def wrapper(n):
            if n not in cache:
                cache[n] = func(n)
            return cache[n]
        return wrapper
    
    @memoize
    def fibonacci_memo(num):
        if num <= 1:
            return num
        return fibonacci_memo(num-1) + fibonacci_memo(num-2)
    
    def is_prime_fibonacci(num):
        if num == 0:
            return False
        fibonacci_num = fibonacci_memo(num)
        if is_prime(fibonacci_num):
            return True
        return False
    
    if n < 1 or not isinstance(n, int):
        return "Invalid Input"
    
    i = 0
    count = 0
    while count < n:
        if is_prime_fibonacci(i):
            count += 1
        i += 1
    if count == n:
        return fibonacci_memo(i-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

if __name__ == '__main__':
    unittest.main()