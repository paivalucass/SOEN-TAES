def big_sum(nums):
    try:
        if len(nums) == 0:
            return "Error Message: Input array is empty"
        else:
            return max(nums) + min(nums)
    except TypeError:
        return "Error: Non-numeric input in the array"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()