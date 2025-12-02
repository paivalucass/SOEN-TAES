def smallest_change(arr):
    n = len(arr)

    dp = [[0]*n for _ in range(n)]

    for gap in range(1, n):
        l = 0
        for h in range(gap, n):
            if arr[l] == arr[h]:
                dp[l][h] = dp[l+1][h-1]
            else:
                dp[l][h] = min(dp[l][h-1], dp[l+1][h]) + 1
            l += 1

    return dp[0][n-1]
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()