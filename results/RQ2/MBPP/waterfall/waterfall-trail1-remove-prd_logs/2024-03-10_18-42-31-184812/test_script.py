def big_diff(nums):
    if not nums:
        return "Empty input list"

    max_num = max(nums)
    min_num = min(nums)

    return max_num - min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()