def max_sum(arr):
    if len(arr) < 3:
        return 0

    increasing_sequence = [0] * len(arr)
    decreasing_sequence = [0] * len(arr)

    for i in range(len(arr)):
        increasing_sequence[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                increasing_sequence[i] = max(increasing_sequence[i], increasing_sequence[j] + arr[i])

    for i in range(len(arr) - 1, -1, -1):
        decreasing_sequence[i] = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                decreasing_sequence[i] = max(decreasing_sequence[i], decreasing_sequence[j] + arr[i])

    max_sum = 0
    for i in range(len(arr)):
        max_sum = max(max_sum, increasing_sequence[i] + decreasing_sequence[i] - arr[i])

    return max_sum
import unittest

class Test(unittest.TestCase):
    def test_max_sum(self):
        self.assertEqual(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]), 194)

if __name__ == '__main__':
    unittest.main()