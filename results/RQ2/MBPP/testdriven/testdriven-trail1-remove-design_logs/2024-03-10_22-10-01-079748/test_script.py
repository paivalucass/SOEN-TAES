def max_subarray_product(arr):
    '''Write a function to find the maximum product subarray of the given array.
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112'''
    
    if len(arr) == 0:
        return 0  # Return 0 if the array is empty
    
    max_ending_here = arr[0]  # Initialize max_ending_here with the first element of the array
    min_ending_here = arr[0]  # Initialize min_ending_here with the first element of the array
    max_so_far = arr[0]  # Initialize max_so_far with the first element of the array
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here  # Swap max_ending_here and min_ending_here if the current element is negative
        max_ending_here = max(arr[i], max_ending_here * arr[i])  # Update max_ending_here based on the current element and the product so far
        min_ending_here = min(arr[i], min_ending_here * arr[i])  # Update min_ending_here based on the current element and the product so far
        
        max_so_far = max(max_so_far, max_ending_here)  # Update max_so_far with the maximum value between max_so_far and max_ending_here
    
    return max_so_far  # Return the maximum product subarray
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()