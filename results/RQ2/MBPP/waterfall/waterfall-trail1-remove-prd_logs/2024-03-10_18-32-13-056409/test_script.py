def lps(input_string):
    if not input_string:
        return 0
    
    n = len(input_string)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if input_string[i] == input_string[j] and length == 2:
                dp[i][j] = 2
            elif input_string[i] == input_string[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
    return dp[0][n - 1]
import unittest

class TestLPS(unittest.TestCase):
    def test_lps(self):
        self.assertEqual(lps("TENS FOR TENS"), 5)

if __name__ == '__main__':
    unittest.main()