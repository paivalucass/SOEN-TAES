def max_sum_increasing_subseq(a, n, index, k):
  dp = [0] * (n + 1)
  for i in range(1, n + 1):
    dp[i] = a[i-1]
    for j in range(1, i):
      if a[i-1] > a[j-1] and i <= k:
        dp[i] = max(dp[i], dp[j] + a[i-1])
  return max(dp)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()