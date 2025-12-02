def big_diff(nums):
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError
    if len(nums) == 0:
        return 0
    return max(nums) - min(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()