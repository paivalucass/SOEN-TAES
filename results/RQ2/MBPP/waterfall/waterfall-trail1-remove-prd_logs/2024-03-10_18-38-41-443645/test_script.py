def positive_count(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers")
    
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("All elements in the list must be integers")
    
    if len(nums) == 0:
        return 0.0
    
    positive_count = sum(1 for num in nums if num > 0)
    return round(float(positive_count) / len(nums), 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()