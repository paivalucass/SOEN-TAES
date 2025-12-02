def zero_count(nums):
    zero_count = sum(1 for i in nums if i == 0)
    non_zero_count = sum(1 for i in nums if i != 0)
    
    if non_zero_count == 0 or zero_count == 0:
        return 0
    else:
        return round(zero_count / non_zero_count, 6) # Rounding to 6 decimal places
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()