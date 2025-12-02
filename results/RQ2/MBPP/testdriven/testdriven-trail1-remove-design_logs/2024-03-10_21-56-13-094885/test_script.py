def bell_number(n):
    if n == 0:
        return 1
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()