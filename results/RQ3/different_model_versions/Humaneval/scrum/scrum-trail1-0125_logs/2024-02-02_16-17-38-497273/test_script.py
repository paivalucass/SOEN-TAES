def fibfib(n: int):
    if not isinstance(n, int) or n < 0:
        return "Input must be a non-negative integer."

    memo = {}

    def fib(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1

        result = fib(n-1) + fib(n-2) + fib(n-3)
        memo[n] = result
        return result

    return fib(n)
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()