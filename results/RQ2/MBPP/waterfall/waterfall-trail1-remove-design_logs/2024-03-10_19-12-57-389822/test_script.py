def max_sum_increasing_subseq(arr, n, index, k):
    dp = [0] * n
    dp[index] = arr[index]
    for i in range(index+1, n):
        for j in range(index, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    if k > index:
        return max(dp) + arr[k]
    else:
        return max(dp)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6), 11)

if __name__ == '__main__':
    unittest.main()