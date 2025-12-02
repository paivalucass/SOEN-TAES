def positive_count(nums):
    if not nums or not all(isinstance(i, int) for i in nums):
        raise ValueError("Input array is empty or doesn't contain any integers")
    
    positive_nums = sum(1 for i in nums if i > 0)
    total_nums = len(nums)

    if total_nums == 0:
        return 0
    else:
        return round(positive_nums / total_nums, 2) # returns ratio rounded to 2 decimal places
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()