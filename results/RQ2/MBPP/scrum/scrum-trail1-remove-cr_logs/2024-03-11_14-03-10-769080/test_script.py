def odd_position(nums):
    if not nums:
        return False
    for i in range(1, len(nums), 2):
        if nums[i] % 2 == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_odd_position(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()