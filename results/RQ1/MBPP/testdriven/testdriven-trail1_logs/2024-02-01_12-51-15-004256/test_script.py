def max_subarray_product(arr):
    '''Write a function to find the maximum product subarray of the given array.'''
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    
    max_product_ending_here = arr[0]
    min_product_ending_here = arr[0]
    max_product_so_far = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product_ending_here, min_product_ending_here = min_product_ending_here, max_product_ending_here
        
        max_product_ending_here = max(arr[i], max_product_ending_here * arr[i])
        min_product_ending_here = min(arr[i], min_product_ending_here * arr[i])
        
        max_product_so_far = max(max_product_so_far, max_product_ending_here)
    
    return max_product_so_far

assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()