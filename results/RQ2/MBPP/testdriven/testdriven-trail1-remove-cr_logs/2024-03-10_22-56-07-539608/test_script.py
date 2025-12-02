def find_sum(arr):
    ''' 
    Write a python function to find the sum of non-repeated elements in a given list. 
    This function should only consider non-repeated elements when calculating the sum. 
     
    :param arr: Input list of elements 
    :return: Sum of non-repeated elements 
    
    Example:
    assert find_sum([1,2,3,1,1,4,5,6]) == 21 
    ''' 
    if not isinstance(arr, list) or len(arr) == 0:
        return 0  # Handle empty list or non-list input
    
    unique_elements = set(arr)  # Using set to store unique elements 
    sum_of_non_repeated = sum(unique_elements) 
    return sum_of_non_repeated 

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()