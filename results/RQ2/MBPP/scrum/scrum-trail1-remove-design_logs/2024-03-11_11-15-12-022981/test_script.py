def odd_position(nums):
    return all(num % 2 != 0 for num in nums[1::2])
import unittest

class Test(unittest.TestCase):
    def test_odd_position(self):
        self.assertTrue(odd_position([2,1,4,3,6,7,6,3]))

if __name__ == '__main__':
    unittest.main()