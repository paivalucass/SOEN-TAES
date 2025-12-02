def sum_negativenum(nums):
    if not nums or all(num >= 0 for num in nums):
        return 0
    else:
        return sum(num for num in nums if num < 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]), -32)

if __name__ == '__main__':
    unittest.main()