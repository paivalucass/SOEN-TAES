def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fib_10(self):
        self.assertEqual(fib(10), 55)

    def test_fib_1(self):
        self.assertEqual(fib(1), 1)

    def test_fib_8(self):
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()