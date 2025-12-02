def zero_count(nums):
    if len(nums) == 0:
        return "Error: Empty array"
    
    zero_count = 0
    non_zero_count = 0
    
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    
    if non_zero_count == 0:
        return "Error: Division by zero"
    else:
        return zero_count / non_zero_count
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, delta=0.001)

if __name__ == '__main__':
    unittest.main()