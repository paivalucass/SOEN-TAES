def specialFilter(nums):
    if not isinstance(nums, list) or not all(isinstance(x, (int, float)) for x in nums):
        raise ValueError("Input must be an array of numbers")

    if not nums:
        return 0

    filtered_nums = [num for num in nums if num > 10 and str(num)[0] in ['1', '3', '5', '7', '9'] and str(num)[-1] in ['1', '3', '5', '7', '9']]
    
    return len(filtered_nums)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    
    def test2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()