def big_diff(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")
    if len(nums) < 1:
        raise ValueError("Input list must not be empty")

    for num in nums:
        if not isinstance(num, (int, float)):
            raise ValueError("Input list must only contain numbers")

    return max(nums) - min(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()