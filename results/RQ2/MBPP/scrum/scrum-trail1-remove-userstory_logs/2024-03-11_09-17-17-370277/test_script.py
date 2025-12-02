def big_diff(nums):
    try:
        if len(nums) <= 1:
            return 0
        else:
            return max(nums) - min(nums)
    except:
        return "Error: Input is not a list of numbers"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_diff([1,2,3,4]), 3)

if __name__ == '__main__':
    unittest.main()