def fibfib(n: int) -> int:
    memo = [0, 0, 1]
    if n <= 2:
        return memo[n]
    for i in range(3, n+1):
        memo.append(memo[i-1] + memo[i-2] + memo[i-3])
    return memo[n]
import unittest

class Test(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)

if __name__ == '__main__':
    unittest.main()