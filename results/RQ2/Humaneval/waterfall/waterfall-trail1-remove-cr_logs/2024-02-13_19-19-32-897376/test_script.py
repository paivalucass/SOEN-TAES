def fib(n: int):
    memo = {}
    def fib_helper(n):
        if n in memo:
            return memo[n]
        if n < 0:
            return "Invalid input"
        if n <= 1:
            return n
        memo[n] = fib_helper(n-1) + fib_helper(n-2)
        return memo[n]
    return fib_helper(n)
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