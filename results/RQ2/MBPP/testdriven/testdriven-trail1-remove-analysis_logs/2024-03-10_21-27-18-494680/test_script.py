def consecutive_duplicates(nums):
    unique_nums = [nums[0]]
    for num in nums:
        if num != unique_nums[-1]:
            unique_nums.append(num)
    return unique_nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()