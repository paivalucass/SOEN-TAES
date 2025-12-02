def comb_sort(nums):
    gap = len(nums)
    shrink = 1.3
    swapped = True

    while gap > 1 or swapped:
        gap = int(gap / shrink)
        swapped = False
        i = 0
        while gap + i < len(nums):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
            i += 1

    return nums
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()