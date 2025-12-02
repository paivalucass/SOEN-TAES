def max_sum(arr):
    n = len(arr)
    left_dp = [0] * n
    right_dp = [0] * n

    for i in range(n):
        left_dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                left_dp[i] = max(left_dp[i], left_dp[j] + arr[i])

    for i in range(n - 1, -1, -1):
        right_dp[i] = arr[i]
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                right_dp[i] = max(right_dp[i], right_dp[j] + arr[i])

    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, left_dp[i] + right_dp[i] - arr[i])

    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()