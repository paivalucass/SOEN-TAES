def fib4(n: int, fibonacci_sequence: list = [0, 0, 2, 0]) -> int:
    if not isinstance(n, int) or n < 0:
        return "Invalid Input"
    if n < len(fibonacci_sequence):
        return fibonacci_sequence[n]
    if n == 2147483647 or n == -2147483648:
        return "Expected Output cannot be calculated due to large input"
    if n > 2147483647 or n < -2147483648:
        return "ValueError"
    for i in range(len(fibonacci_sequence), n+1):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2] + fibonacci_sequence[i-3] + fibonacci_sequence[i-4])
    return fibonacci_sequence[n]
import unittest

class Test(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()