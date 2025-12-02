def fib4(n: int) -> int:
    if n < 4:
        return [0, 0, 2, 0][n]

    fib_values = [0, 0, 2, 0]

    for i in range(4, n+1):
        fib_values[i % 4] = fib_values[0] + fib_values[1] + fib_values[2] + fib_values[3]

    return fib_values[n % 4]
import unittest

class TestFib4(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()