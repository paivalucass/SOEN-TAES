def sum_negativenum(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")
    
    try:
        neg_nums_sum = sum([num for num in nums if num < 0])
        return neg_nums_sum
    except:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()