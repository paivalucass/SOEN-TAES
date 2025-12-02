def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n <= 0:
        return "Error: Invalid input, please enter a positive integer"

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
import unittest

class Test(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()