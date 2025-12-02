def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i + 1][j])
    return dp[0][n - 1]
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()