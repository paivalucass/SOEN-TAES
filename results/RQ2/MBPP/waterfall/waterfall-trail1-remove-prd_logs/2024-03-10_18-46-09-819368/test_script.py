def consecutive_duplicates(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of numbers")

    if len(nums) == 0:
        return []

    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            result.append(nums[i])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4])

if __name__ == '__main__':
    unittest.main()