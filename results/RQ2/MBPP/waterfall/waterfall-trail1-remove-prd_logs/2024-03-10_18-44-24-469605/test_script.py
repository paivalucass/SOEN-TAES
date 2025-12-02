def largest_subset(nums):
    if len(nums) <= 1:
        return len(nums)
    
    max_subset = 1
    remainder_map = [1] * len(nums)
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                remainder_map[i] = max(remainder_map[i], remainder_map[j] + 1)
                remainder_map[j] = max(remainder_map[j], remainder_map[i] + 1)
                max_subset = max(max_subset, remainder_map[i], remainder_map[j])
    
    return max_subset

import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([ 1, 3, 6, 13, 17, 18 ]), 4)

if __name__ == '__main__':
    unittest.main()