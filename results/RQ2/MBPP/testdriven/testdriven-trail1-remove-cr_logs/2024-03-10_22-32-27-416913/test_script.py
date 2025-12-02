def pancake_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        max_index = nums.index(max(nums[:i+1]))
        nums = nums[:max_index+1][::-1] + nums[max_index+1:]
    return nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()