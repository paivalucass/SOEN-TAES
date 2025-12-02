def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[dp[i - 1]] + dp[i - dp[i - 1]]
        return dp[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()