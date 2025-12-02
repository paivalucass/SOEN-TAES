def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n

    for i in range(n):
        inc[i] = arr[i]
        dec[i] = arr[i]

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc[i] = max(inc[i], inc[i-1] + arr[i])

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i+1]:
            dec[i] = max(dec[i], dec[i+1] + arr[i])

    maxSum = 0
    for i in range(n):
        maxSum = max(maxSum, inc[i] + dec[i])

    return maxSum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()