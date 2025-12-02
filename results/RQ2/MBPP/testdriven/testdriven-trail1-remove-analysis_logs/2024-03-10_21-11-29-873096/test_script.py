def zero_count(nums):
    zero_count = nums.count(0)
    non_zero_count = len(nums) - zero_count
    if non_zero_count == 0:
        return 0.000000
    ratio = zero_count / non_zero_count
    return round(ratio, 6)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()