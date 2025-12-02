def comb_sort(nums):
    def get_next_gap(gap):
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return int(gap)

    n = len(nums)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
    
    return nums
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()