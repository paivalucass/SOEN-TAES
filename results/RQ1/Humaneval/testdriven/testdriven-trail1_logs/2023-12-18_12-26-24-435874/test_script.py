def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if not isinstance(n, int):
        raise ValueError("Invalid Input: Input must be an integer")
    if n < 0:
        raise ValueError("Invalid Input: Input must be a non-negative integer")
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()