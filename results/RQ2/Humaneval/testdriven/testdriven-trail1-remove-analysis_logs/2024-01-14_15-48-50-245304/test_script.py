def fib(n: int):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
import unittest

class Test(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)

if __name__ == '__main__':
    unittest.main()