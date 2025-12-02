def big_sum(nums):
    try:
        if len(nums) == 0:
            return "Input Validation Error: Empty list"
        else:
            min_num = min(nums)
            max_num = max(nums)
            return min_num + max_num
    except TypeError:
        return "Input Validation Error: Invalid input type"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()