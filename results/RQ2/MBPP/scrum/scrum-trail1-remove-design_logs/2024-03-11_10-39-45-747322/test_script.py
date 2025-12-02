def positive_count(nums):
    positive_nums = sum(1 for num in nums if num > 0)
    ratio = positive_nums / len(nums)
    return round(ratio, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.54)

if __name__ == '__main__':
    unittest.main()