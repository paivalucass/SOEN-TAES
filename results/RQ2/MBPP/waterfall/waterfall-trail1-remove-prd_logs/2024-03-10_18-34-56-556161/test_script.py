import math
def count_binary_seq(n):
    if n < 0:
        raise ValueError("n should be a non-negative integer")

    dp = [0] * (n * 2 + 1)
    dp[n] = 1

    for i in range(1, n * 2 + 1):
        if i - n - 1 >= 0:
            dp[i] = dp[i - 1] + dp[i - 1] - dp[i - n - 1]
        else:
            dp[i] = dp[i - 1]

    return dp[n]
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_binary_seq(1), 2.0)

if __name__ == '__main__':
    unittest.main()