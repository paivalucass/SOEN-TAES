def positive_count(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")
    
    if len(nums) == 0:
        return 0.0
    else:
        count = sum(1 for num in nums if num > 0)
        return round(float(count) / len(nums), 2)
import unittest

class Test(unittest.TestCase):
    def test_positive_count(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()