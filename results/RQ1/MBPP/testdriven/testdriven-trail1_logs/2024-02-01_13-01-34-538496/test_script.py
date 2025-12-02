def big_diff(nums):
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Input must be a list of numbers")
    
    if len(nums) == 0:
        return 0
    else:
        max_num = max(nums)
        min_num = min(nums)
        return max_num - min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()