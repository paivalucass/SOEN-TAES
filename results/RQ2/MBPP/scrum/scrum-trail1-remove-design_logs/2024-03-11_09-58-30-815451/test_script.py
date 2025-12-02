def comb_sort(nums):
    n = len(nums)
    gap = n
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = max(int(gap / shrink), 1)
        swapped = False
        for i in range(n - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True

    return nums
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()