def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        count = 2
        first = 2
        second = 3
        while count < n:
            next_fib = first + second
            if is_prime(next_fib):
                count += 1
            first, second = second, next_fib
        return next_fib
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