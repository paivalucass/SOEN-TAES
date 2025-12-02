def big_sum(nums):
    if len(nums) < 2:
        return "Array should have at least two numbers"
    else:
        return min(nums) + max(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()