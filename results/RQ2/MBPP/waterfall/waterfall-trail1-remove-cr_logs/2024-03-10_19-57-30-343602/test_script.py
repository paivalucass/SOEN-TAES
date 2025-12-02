def max_sum(arr):
    if len(arr) < 3:
        return 0

    n = len(arr)
    increasing = [0] * n
    decreasing = [0] * n

    for i in range(n):
        increasing[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j] + arr[i])

    for i in range(n - 1, -1, -1):
        decreasing[i] = arr[i]
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + arr[i])

    max_sum_bitonic = 0
    for i in range(n):
        max_sum_bitonic = max(max_sum_bitonic, increasing[i] + decreasing[i] - arr[i])

    return max_sum_bitonic
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()