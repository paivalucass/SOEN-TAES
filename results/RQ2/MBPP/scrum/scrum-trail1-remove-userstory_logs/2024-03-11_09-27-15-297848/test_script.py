def is_odd(num):
    return num % 2 != 0

def odd_position(nums):
    for i in range(1, len(nums), 2):
        if not is_odd(nums[i]):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_odd_position(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()