def sum_negativenum(nums):
    negative_sum = 0
    for num in nums:
        if num < 0:
            negative_sum += num
    return negative_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()