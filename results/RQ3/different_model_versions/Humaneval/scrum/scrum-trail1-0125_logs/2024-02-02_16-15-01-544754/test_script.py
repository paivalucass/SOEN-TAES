def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def is_fibonacci(num: int) -> bool:
    if num < 0:
        return False
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def prime_fib(n: int) -> int:
    if n < 1:
        return None
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num) and is_fibonacci(num):
            count += 1
    return num
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