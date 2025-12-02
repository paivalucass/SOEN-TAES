def sum_negativenum(nums):
    sum_negative = sum([num for num in nums if num < 0])
    return sum_negative
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()