def two_unique_nums(nums):
    return [num for num in nums if nums.count(num) == 1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(two_unique_nums([1,2,3,2,3,4,5]), [1, 4, 5])

if __name__ == '__main__':
    unittest.main()