def consecutive_duplicates(nums):
    result = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            result.append(nums[i])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()