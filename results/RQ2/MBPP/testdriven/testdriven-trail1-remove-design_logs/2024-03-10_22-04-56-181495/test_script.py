def count_binary_seq(n):
    # Initialize a 2D array to store the counts of binary sequences
    dp = [[0] * (2*n + 1) for _ in range(2*n + 1)]

    # Base case: when n = 0
    dp[0][0] = 1

    # Fill in the dp array using dynamic programming approach
    for i in range(1, 2*n + 1):
        for j in range(2*n + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][1]
            elif j == 2*n:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    # The count of binary sequences where the sum of first n bits is same as the sum of last n bits is the sum of the last row of the dp array
    count = sum(dp[-1])

    return count

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(count_binary_seq(1), 2.0, delta=0.001)

if __name__ == '__main__':
    unittest.main()