def zero_count(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers")
    if len(nums) == 0:
        raise ValueError("Input list cannot be empty")
    
    zero_count = sum(1 for i in nums if i == 0)
    non_zero_count = sum(1 for i in nums if i != 0)
    
    if non_zero_count == 0:
        return float('inf')  
    else:
        return zero_count / non_zero_count
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()