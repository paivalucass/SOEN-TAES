def minSubArraySum(nums):
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    
    return min_sum

import unittest

class Test(unittest.TestCase):
    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()