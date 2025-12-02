def max_sum_increasing_subseq(a, n, index, k):
    if n <= 0 or index < 0 or index >= n or k <= index or k >= n:
        return "Invalid input"

    dp = [0] * n
    dp[index] = a[index]

    for i in range(index+1, k+1):
        for j in range(index, i):
            if a[i] > a[j] and dp[i] < dp[j] + a[i]:
                dp[i] = dp[j] + a[i]

    return dp[k]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()