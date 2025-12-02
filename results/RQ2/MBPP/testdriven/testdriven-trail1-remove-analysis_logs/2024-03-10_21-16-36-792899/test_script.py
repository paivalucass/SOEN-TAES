def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    dp[0] = a[0]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j] and dp[i] < dp[j] + a[i]:
                dp[i] = dp[j] + a[i]
    return max(dp[:index+1]) + a[k] if k > index else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()