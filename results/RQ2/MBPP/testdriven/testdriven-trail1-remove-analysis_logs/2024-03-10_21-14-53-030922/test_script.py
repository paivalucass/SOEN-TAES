def sum_even_and_even_index(arr):
    ''' 
    Write a python function to find the sum of even numbers at even positions of a list. 
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30 
    '''
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")
    
    # Check if list is not empty
    if not arr:
        raise ValueError("Input list is empty")
    
    # Check if list contains only numbers
    for num in arr:
        if not isinstance(num, int):
            raise TypeError("List should contain only numbers")
    
    even_sum = 0
    for i in range(len(arr)):
        # Check if index is even and the number at that index is even
        if i % 2 == 0 and arr[i] % 2 == 0:
            even_sum += arr[i]
    
    return even_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()