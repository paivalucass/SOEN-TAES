def pancake_sort(nums):
    if not nums or not all(isinstance(x, (int, float)) for x in nums):
        return []

    def flip(arr, k):
        arr[:k] = arr[:k][::-1]

    for i in range(len(nums)-1, 0, -1):
        max_index = nums.index(max(nums[:i+1]))
        flip(nums, max_index+1)
        flip(nums, i+1)

    return nums
import unittest

class Test(unittest.TestCase):
    def test_pancake_sort(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()