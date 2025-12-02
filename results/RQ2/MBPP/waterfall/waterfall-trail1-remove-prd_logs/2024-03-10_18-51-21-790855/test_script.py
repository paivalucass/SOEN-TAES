import math

def count_binary_seq(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")

    dp = [[0] * (n*2+1) for _ in range(n+1)]
    dp[0][n] = 1

    for i in range(1, n+1):
        for j in range(n*2+1):
            dp[i][j] = dp[i-1][j]
            if j >= i:
                dp[i][j] += dp[i-1][j-i]

    return dp[n][n]
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_binary_seq(1), 2.0)

if __name__ == '__main__':
    unittest.main()