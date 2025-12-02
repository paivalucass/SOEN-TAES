def odd_position(nums):
    flag = True
    for i in range(1, len(nums), 2):
        if nums[i] % 2 == 0:
            flag = False
    return flag
import unittest

class Test(unittest.TestCase):
    def test_odd_position(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()