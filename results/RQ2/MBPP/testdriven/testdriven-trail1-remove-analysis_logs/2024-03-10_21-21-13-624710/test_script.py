def max_subarray_product(arr):
    '''
    Write a function to find the maximum product subarray of the given array.
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
    '''

    # Initialize variables with first element of array
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]

    # Iterate through the array and update max_prod, min_prod, and result accordingly
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(arr[i], max_prod * arr[i])
        min_prod = min(arr[i], min_prod * arr[i])
        
        result = max(result, max_prod)
    
    # Return the maximum product subarray
    return result
import unittest

class TestMaxSubarrayProduct(unittest.TestCase):
    def test_max_subarray_product(self):
        self.assertEqual(max_subarray_product([1, -2, -3, 0, 7, -8, -2]), 112)

if __name__ == '__main__':
    unittest.main()