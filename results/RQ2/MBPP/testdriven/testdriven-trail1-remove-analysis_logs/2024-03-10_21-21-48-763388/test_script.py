def big_sum(nums):
    '''Write a python function to find the sum of the largest and smallest value in a given array.
    assert big_sum([1,2,3]) == 4'''
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0] * 2
    else:
        return max(nums) + min(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()