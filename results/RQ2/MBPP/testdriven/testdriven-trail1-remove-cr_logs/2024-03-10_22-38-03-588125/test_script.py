def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    for i in range(index, k):
        for j in range(index, i):
            if a[i] > a[j] and dp[i] < dp[j] + a[i]:
                dp[i] = dp[j] + a[i]
    return max(dp)
import unittest

class Test(unittest.TestCase):
    def test_max_sum_increasing_subseq(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()