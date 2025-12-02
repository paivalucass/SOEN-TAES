from typing import List

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_square(x: int) -> bool:
    sqrt_x = int(x**0.5)
    return sqrt_x * sqrt_x == x

def is_fibonacci(num: int) -> bool:
    return is_perfect_square(5*num*num + 4) or is_perfect_square(5*num*num - 4)

def prime_fib(n: int) -> int:
    if n < 1:
        return "Invalid input"
    if n == 1:
        return 2
    count = 1
    num = 2
    while count < n:
        num += 1
        if is_fibonacci(num) and is_prime(num):
            count += 1
    return num

# Test cases
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
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