def zero_count(nums):
    if not nums:
        return 0.0
    zero_count = sum(1 for num in nums if num == 0)
    non_zero_count = sum(1 for num in nums if num != 0)
    return zero_count / non_zero_count if non_zero_count != 0 else 1.0
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, delta=0.001)

if __name__ == '__main__':
    unittest.main()