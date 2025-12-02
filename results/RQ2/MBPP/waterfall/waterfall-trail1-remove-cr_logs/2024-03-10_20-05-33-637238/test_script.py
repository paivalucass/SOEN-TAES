def positive_count(nums):
    if nums is None or len(nums) == 0:
        return 0.0 
    
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("Input array should contain only integers")
    
    positive_count = sum(1 for num in nums if num > 0)
    
    ratio = positive_count / len(nums)
    
    return round(ratio, 2)  # Return the ratio rounded to 2 decimal places
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()