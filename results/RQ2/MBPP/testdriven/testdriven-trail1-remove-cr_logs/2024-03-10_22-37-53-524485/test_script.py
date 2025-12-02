def count_binary_seq(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 2
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n + 1):
        dp[i] = 2 * dp[i - 1] + dp[i - 2]
    
    return dp[n]
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()