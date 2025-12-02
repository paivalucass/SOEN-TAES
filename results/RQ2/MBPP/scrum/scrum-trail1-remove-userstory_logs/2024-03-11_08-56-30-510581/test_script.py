def sum_negativenum(nums):
    '''Write a function to calculate the sum of the negative numbers of a given list of numbers.'''
    negative_sum = 0
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not nums:
        raise ValueError("Input list is empty")
    
    for num in nums:
        if num < 0:
            negative_sum += num
    
    return negative_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()