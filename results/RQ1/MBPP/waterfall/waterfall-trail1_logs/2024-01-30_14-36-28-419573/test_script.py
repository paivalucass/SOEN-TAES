def big_sum(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        min_val = min(nums)
        max_val = max(nums)
        sum_of_min_and_max = min_val + max_val
        return sum_of_min_and_max
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()