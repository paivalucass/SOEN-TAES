def max_sub_array_sum(arr, size):
    '''Write a function to find the sum of the largest contiguous sublist in the given list.
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7'''
    
    max_subarray_sum = arr[0]
    current_subarray_sum = arr[0]
    
    for i in range(1, size):
        current_subarray_sum = max(arr[i], current_subarray_sum + arr[i])
        max_subarray_sum = max(max_subarray_sum, current_subarray_sum)
    
    return max_subarray_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()