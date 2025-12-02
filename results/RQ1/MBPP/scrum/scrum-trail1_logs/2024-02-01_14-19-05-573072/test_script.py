def comb_sort(nums):
    gap = len(nums)
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = max(int(gap / shrink), 1)
        swapped = False
        for i in range(len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
    return nums

assert comb_sort([]) == []
assert comb_sort([5]) == [5]
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
assert comb_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert comb_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
assert comb_sort([5, 15, 5, 25, 15]) == [5, 5, 15, 15, 25]
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()