def zero_count(nums):
    zero_count = 0
    non_zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    return round(zero_count / non_zero_count, 6) # rounding to 6 decimal places to match the expected output

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()