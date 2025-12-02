def max_sum(arr):
    n = len(arr)
    increasing = [0] * n
    decreasing = [0] * n

    increasing[0] = arr[0]
    for i in range(1, n):
        increasing[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and increasing[i] < increasing[j] + arr[i]:
                increasing[i] = increasing[j] + arr[i]

    decreasing[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        decreasing[i] = arr[i]
        for j in range(i + 1, n):
            if arr[i] > arr[j] and decreasing[i] < decreasing[j] + arr[i]:
                decreasing[i] = decreasing[j] + arr[i]

    max_sum = 0
    for i in range(n):
        if max_sum < increasing[i] + decreasing[i] - arr[i]:
            max_sum = increasing[i] + decreasing[i] - arr[i]

    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()