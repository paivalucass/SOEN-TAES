def count_binary_seq(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_binary_seq(1), 2.0)

if __name__ == '__main__':
    unittest.main()