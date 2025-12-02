def max_sub_array_sum(a, size):
    '''Write a function to find the sum of the largest contiguous sublist in the given list.
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7'''
    
    # Initialize variables
    max_so_far = a[0]  # Initialize max_so_far with first element of the list
    curr_max = a[0]    # Initialize curr_max with first element of the list
    
    # Loop through the list to find the maximum sum
    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])  # Update curr_max with the maximum of current element and sum of current element and curr_max
        max_so_far = max(max_so_far, curr_max)  # Update max_so_far with the maximum of max_so_far and curr_max
        
    return max_so_far  # Return the maximum sum of contiguous sublist
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()