def maxAverageOfPath(cost):
    if not cost or not cost[0]:  # Check for empty matrix
        return 0
    
    n = len(cost)
    m = len(cost[0])
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = cost[0][0]

    # Fill the first row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    # Fill the first column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Fill the rest of the dp table
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]

    return dp[n - 1][m - 1] / (n + m - 1)  # Return the maximum average value

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()