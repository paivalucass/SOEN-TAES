def big_sum(nums):
    if not isinstance(nums, list):
        return "Error: Invalid Input"
    elif not nums:
        return "Error: Empty Array"
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(nums) + min(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()