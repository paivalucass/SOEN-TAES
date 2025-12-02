def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """

    if n <= 0:
        return "Error: Invalid input"

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    result = 0
    count = 0
    while count < n:
        if is_prime(fib[count]) and count < n-1:
            count += 1
        elif is_prime(fib[count]) and count == n-1:
            result = fib[count]
            count += 1
        else:
            count += 1

    return result
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