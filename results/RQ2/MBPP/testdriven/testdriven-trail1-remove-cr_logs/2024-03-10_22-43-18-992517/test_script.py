def max_product(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [0] * n

    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] * arr[i])

    return max(dp)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()