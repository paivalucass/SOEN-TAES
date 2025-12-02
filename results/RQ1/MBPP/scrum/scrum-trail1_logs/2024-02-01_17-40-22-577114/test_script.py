def largest_subset(arr):
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] % arr[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 3, 6, 13, 17, 18]), 4)

if __name__ == '__main__':
    unittest.main()