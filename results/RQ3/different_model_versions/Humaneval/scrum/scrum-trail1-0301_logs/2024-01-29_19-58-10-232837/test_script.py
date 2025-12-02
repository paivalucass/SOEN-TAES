def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        return "Error: Input array should contain only integers"

    if len(arr) == 0:
        return "Error: Empty array is not allowed"

    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else min(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1]) + 1

    return dp[0][n - 1]
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()