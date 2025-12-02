def maxAverageOfPath(cost):
    if not cost or not cost[0]:
        return 0  # If the matrix is empty

    n = len(cost)
    m = len(cost[0])

    # Initialize a 2D array to store the maximum average
    dp = [[0] * m for _ in range(n)]

    # Calculate the maximum average path using dynamic programming
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = cost[i][j]
            elif i == 0:
                dp[i][j] = (dp[i][j - 1] * j + cost[i][j]) / (j + 1)
            elif j == 0:
                dp[i][j] = (dp[i - 1][j] * i + cost[i][j]) / (i + 1)
            else:
                dp[i][j] = max((dp[i - 1][j] * (i+1) + dp[i][j - 1] * (j+1) + cost[i][j]) / (i+1+j+1),
                               (dp[i][j - 1] * (j+1) + dp[i - 1][j] * (i+1) + cost[i][j]) / (i+1+j+1))

    return dp[n - 1][m - 1]  # Return the maximum average path from top-left to bottom-right cell.
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()