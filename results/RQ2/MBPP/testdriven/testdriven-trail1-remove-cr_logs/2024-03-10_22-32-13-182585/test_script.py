def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    powers = [2 ** i for i in range(n+1)]
    dp = [False] * (n + 1)
    dp[0] = True
    for power in powers:
        for i in range(n, power - 1, -1):
            dp[i] = dp[i] or dp[i - power]
    return dp[n]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Sum_Of_Powers_Of_Two(10), True)

if __name__ == '__main__':
    unittest.main()