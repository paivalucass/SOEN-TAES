def positive_count(nums):
    if nums is None or not isinstance(nums, list) or not all(isinstance(n, (int, float)) for n in nums):
        raise ValueError("Input is not a valid list of numbers")
    
    positive_nums = [num for num in nums if num > 0]
    ratio = len(positive_nums) / len(nums)
    return round(ratio, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()