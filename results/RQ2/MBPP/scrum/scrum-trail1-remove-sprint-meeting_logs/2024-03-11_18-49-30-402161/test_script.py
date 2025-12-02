def max_subarray_product(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    max_end_here = arr[0]
    min_end_here = arr[0]
    max_so_far = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_end_here, min_end_here = min_end_here, max_end_here
            
        max_end_here = max(arr[i], max_end_here * arr[i])
        min_end_here = min(arr[i], min_end_here * arr[i])
        
        max_so_far = max(max_so_far, max_end_here)
        
    return max_so_far

# Test Cases
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([-2, -3, -7, -8]) == 336
assert max_subarray_product([2, 3, 7, 8]) == 336
assert max_subarray_product([]) == 0
assert max_subarray_product([5]) == 5
assert max_subarray_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 2432902008176640000
assert max_subarray_product([-1, -2, 3, -4, 5, -6]) == 720
assert max_subarray_product([0, 0, 0, 0, 0]) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()