def max_product(arr):
    n = len(arr)
    max_ending_here = arr[0]
    min_ending_here = arr[0]
    max_so_far = arr[0]
    for i in range(1, n):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here
        max_ending_here = max(arr[i], max_ending_here * arr[i])
        min_ending_here = min(arr[i], min_ending_here * arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_product([3, 100, 4, 5, 150, 6]), 3000)

if __name__ == '__main__':
    unittest.main()