def big_sum(nums):
    if not isinstance(nums, list):
        return "Error: Input is not a list"
    if len(nums) < 2:
        return "Error: Input list must have at least two elements"

    min_val = min(nums)
    max_val = max(nums)
    return min_val + max_val
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()