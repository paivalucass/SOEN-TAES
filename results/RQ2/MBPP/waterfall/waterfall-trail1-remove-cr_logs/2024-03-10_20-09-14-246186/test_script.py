def two_unique_nums(nums):
    unique_nums = [x for x in nums if nums.count(x) == 1]
    return unique_nums

assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(two_unique_nums([1,2,3,2,3,4,5]), [1, 4, 5])

if __name__ == '__main__':
    unittest.main()