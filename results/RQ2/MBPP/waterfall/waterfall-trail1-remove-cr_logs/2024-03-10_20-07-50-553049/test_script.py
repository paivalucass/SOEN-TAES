def big_sum(nums):
    sorted_nums = sorted(nums)
    sum_of_extreme_values = sorted_nums[0] + sorted_nums[-1]
    return sum_of_extreme_values
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()