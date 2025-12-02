def big_diff(nums):
    if not isinstance(nums, list) or len(nums) < 2 or not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Input must be a non-empty list containing at least two numeric values")

    difference = max(nums) - min(nums)

    return difference
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()