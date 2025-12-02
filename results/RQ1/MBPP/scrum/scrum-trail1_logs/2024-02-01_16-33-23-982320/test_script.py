def maxAverageOfPath(cost):
    N = len(cost)
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = cost[0][0]
    
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + cost[i][0]
        dp[0][i] = dp[0][i-1] + cost[0][i]
    
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    
    return dp[-1][-1] / (2*N-1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]), 5.2)

if __name__ == '__main__':
    unittest.main()