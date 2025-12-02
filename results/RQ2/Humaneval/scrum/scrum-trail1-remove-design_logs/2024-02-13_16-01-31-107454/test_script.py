def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    if n <= 0 or not isinstance(n, int):
        return "Invalid Input"
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        count = 2
        while count < n:
            c = a + b
            a, b = b, c
            if is_prime(c):
                count += 1
        return c
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