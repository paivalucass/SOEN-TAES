def count_no_of_ways(n, k):
    dp = [0] * (n + 1)
    dp[1] = k
    same = 0
    diff = k
    for i in range(2, n + 1):
        same = diff
        diff = dp[i - 1] * (k - 1)
        dp[i] = same + diff
    return dp[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_no_of_ways(2, 4), 16)

if __name__ == '__main__':
    unittest.main()