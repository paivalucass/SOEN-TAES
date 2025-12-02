def comb_sort(nums):
    gap = len(nums)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        else:
            sorted = False

        i = 0
        while i + gap < len(nums):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                sorted = False
            i += 1

    return nums

import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()