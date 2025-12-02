def minSubArraySum(nums):
    min_sum = float('inf')
    curr_sum = 0
    for num in nums:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)
    return min_sum
import unittest

class Test(unittest.TestCase):
    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()