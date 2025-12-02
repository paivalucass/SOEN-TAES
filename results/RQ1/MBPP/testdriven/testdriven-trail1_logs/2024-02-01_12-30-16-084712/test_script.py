def count_binary_seq(n):
    '''Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.'''

    def count_binary_seq_dp(n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]

    return count_binary_seq_dp(n)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(count_binary_seq(1), 2.0, delta=0.001)

if __name__ == '__main__':
    unittest.main()