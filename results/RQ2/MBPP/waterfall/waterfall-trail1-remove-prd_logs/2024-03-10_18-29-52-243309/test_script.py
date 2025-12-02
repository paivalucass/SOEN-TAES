def zero_count(nums):
    try:
        zero_count = nums.count(0)
        non_zero_count = len(nums) - zero_count
        ratio = zero_count / non_zero_count
        return ratio
    except ZeroDivisionError:
        return 0.0
    except:
        raise ValueError("Input must be an array of integers")
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, places=6)

if __name__ == '__main__':
    unittest.main()