def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = cost[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + cost[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + cost[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
    max_average = dp[n - 1][n - 1] / (2 * n - 1)
    return max_average

assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()