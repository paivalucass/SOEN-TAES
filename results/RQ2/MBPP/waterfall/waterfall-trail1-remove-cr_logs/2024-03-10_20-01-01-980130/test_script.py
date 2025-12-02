def max_sum_increasing_subseq(a, n, index, k):
    max_sum = 0
    dp = [0] * n
    for i in range(n):
        dp[i] = a[i]
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])
        if i == index and k > index:
            dp[i] += a[k]
            dp[i] = max(dp[i], dp[k])
        max_sum = max(max_sum, dp[i])
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()