def max_sum_increasing_subseq(a, n, index, k):
    if n == 0:
        return 0

    dp = [0] * n
    dp[index] = a[index]

    for j in range(index+1, n):
        for l in range(index, j):
            if a[j] > a[l]:
                dp[j] = max(dp[j], dp[l] + a[j])

    return max(dp)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()