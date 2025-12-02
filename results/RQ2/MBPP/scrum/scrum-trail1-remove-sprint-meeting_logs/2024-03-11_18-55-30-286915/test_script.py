def big_diff(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return 0
    if not all(isinstance(n, (int, float)) for n in nums):
        raise TypeError("Input must be a list of numbers")
    
    max_val = max(nums)
    min_val = min(nums)
    
    return max_val - min_val
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()