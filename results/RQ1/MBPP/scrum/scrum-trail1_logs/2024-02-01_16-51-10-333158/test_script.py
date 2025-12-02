def odd_position(nums):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise TypeError("Input must be a list of integers")
    if not nums:
        return False
    for index in range(1, len(nums), 2):
        if nums[index] % 2 == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_position([2,1,4,3,6,7,6,3]), True)

if __name__ == '__main__':
    unittest.main()