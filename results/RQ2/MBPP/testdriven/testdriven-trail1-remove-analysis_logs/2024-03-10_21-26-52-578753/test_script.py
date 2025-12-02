def maxAverageOfPath(cost):
    n = len(cost)
    if n == 0:
        return 0
    m = len(cost[0])
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = cost[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + cost[i][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + cost[0][j]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
    return dp[-1][-1] / (n + m - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()