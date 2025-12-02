def eulerian_num(n, m):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = (j+1) * dp[i-1][j] + (i-j) * dp[i-1][j-1]
    return dp[n][m]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()