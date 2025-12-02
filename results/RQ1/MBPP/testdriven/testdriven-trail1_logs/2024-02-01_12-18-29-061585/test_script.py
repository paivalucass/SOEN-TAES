def max_sum(arr):
    increasing = [0] * len(arr)
    decreasing = [0] * len(arr)

    for i in range(len(arr)):
        increasing[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j] + arr[i])

    for i in range(len(arr) - 1, -1, -1):
        decreasing[i] = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + arr[i])

    max_sum = 0
    for i in range(len(arr)):
        max_sum = max(max_sum, increasing[i] + decreasing[i] - arr[i])

    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()