def max_subarray_product(arr):
    max_end = arr[0]
    min_end = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_end, min_end = min_end, max_end
        
        max_end = max(arr[i], max_end * arr[i])
        min_end = min(arr[i], min_end * arr[i])
        
        max_so_far = max(max_so_far, max_end)

    return max_so_far
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()