def zero_count(nums):
    count_zeros = 0
    count_non_zeros = 0
    
    for num in nums:
        if num == 0:
            count_zeros += 1
        else:
            count_non_zeros += 1
    
    if count_non_zeros == 0:
        return 0.0
    else:
        return round(count_zeros / count_non_zeros, 6) # rounding to 6 decimal places for ratio
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()