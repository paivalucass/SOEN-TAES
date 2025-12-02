def lps(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input - long string",
      "Input Data": "TENS FOR TENS",
      "Expected Output": 5
    },
    {
      "Test Title": "Valid input - short string",
      "Input Data": "abcba",
      "Expected Output": 5
    },
    {
      "Test Title": "Edge case - empty string",
      "Input Data": "",
      "Expected Output": 0
    },
    {
      "Test Title": "Edge case - single character string",
      "Input Data": "a",
      "Expected Output": 1
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lps("TENS FOR TENS"), 5)

if __name__ == '__main__':
    unittest.main()