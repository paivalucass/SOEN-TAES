def fibfib(n: int) -> int:
    if n < 0:
        raise ValueError("Input value cannot be negative")
    memo = [0, 0, 1] + [0] * (n - 2)
    for i in range(3, n+1):
        if memo[i] == 0:
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()