def two_unique_nums(nums):
    """
    Write a python function to remove duplicate numbers from a given list of numbers
    """
    if not isinstance(nums, list):
        return "Input should be a list of numbers"
    
    if len(nums) <= 1:
        return "Input list should have at least two numbers"
    
    unique_list = list(set(nums))
    return unique_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(two_unique_nums([1,2,3,2,3,4,5]), [1, 4, 5])

if __name__ == '__main__':
    unittest.main()