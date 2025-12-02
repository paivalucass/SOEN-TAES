def lps(str):
    n = len(str)
    dp = [[0 for x in range(n)] for y in range(n)]
 
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if str[i] == str[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
 
    return dp[0][n-1]
import unittest

class Test(unittest.TestCase):
    def test_lps(self):
        self.assertEqual(lps("TENS FOR TENS"), 5)

if __name__ == '__main__':
    unittest.main()