def positive_count(nums):
    '''Write a function to find the ratio of positive numbers in an array of integers.'''
    
    # Input validation and error handling for empty input array
    if len(nums) == 0:
        return 0.00
    
    # Use filter and len functions to count positive numbers and total numbers
    positive_count = len(list(filter(lambda x: x > 0, nums)))
    total_count = len(nums)
    
    # Calculate the ratio of positive numbers
    ratio = positive_count / total_count
    
    # Return the ratio with a precision of two decimal places
    return round(ratio, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()