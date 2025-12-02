def pancake_sort(nums):
    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of numbers")

    if len(nums) <= 1:
        return nums

    for i in range(len(nums)-1, 0, -1):
        max_idx = nums.index(max(nums[:i+1]))
        if max_idx != i:
            nums = nums[:max_idx+1][::-1] + nums[max_idx+1:]
            nums = nums[:i+1][::-1] + nums[i+1:]

    return nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()