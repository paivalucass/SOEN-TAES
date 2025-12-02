def sum_negativenum(nums):
    if not isinstance(nums, list):
        return "Error: Input is not a list"
    if len(nums) == 0:
        return 0

    sum_negative = 0
    for num in nums:
        if isinstance(num, (int, float)):
            if num < 0:
                sum_negative += num

    return sum_negative
import unittest

class Test(unittest.TestCase):
    def test_sum_negativenum(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()