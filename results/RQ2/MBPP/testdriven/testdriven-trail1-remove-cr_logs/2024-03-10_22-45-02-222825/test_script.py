def two_unique_nums(nums):
    """
    Write a python function to remove duplicate numbers from a given list of numbers.
    
    Args:
    nums (list): List of numbers
    
    Returns:
    list: A new list containing only the unique numbers from the input list
    """
    
    # Error handling for invalid inputs
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")
    
    for num in nums:
        if not isinstance(num, (int, float)):
            raise ValueError("Input list must contain only numeric elements")
    
    return list(set(nums))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(two_unique_nums([1,2,3,2,3,4,5]), [1, 4, 5])

if __name__ == '__main__':
    unittest.main()