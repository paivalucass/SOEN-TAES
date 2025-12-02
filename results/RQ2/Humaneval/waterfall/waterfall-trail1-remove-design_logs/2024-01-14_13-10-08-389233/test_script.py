def fib(n: int) -> int:
    """Return n-th Fibonacci number."""
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 100:
        return "Input must be within the range of 1 to 100."
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
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