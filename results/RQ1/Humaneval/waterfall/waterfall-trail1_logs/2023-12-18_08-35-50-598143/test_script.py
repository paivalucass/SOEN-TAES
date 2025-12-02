def fib4(n: int):
    # Error Handling
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input value must be a non-negative integer")

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d

    return d

# Test cases
print(fib4(0))  # Expected output: 0
print(fib4(1))  # Expected output: 0
print(fib4(2))  # Expected output: 2
print(fib4(3))  # Expected output: 0
print(fib4(5))  # Expected output: 4
print(fib4(6))  # Expected output: 8
print(fib4(7))  # Expected output: 14
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()