def big_diff(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[-1] - sorted_nums[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()