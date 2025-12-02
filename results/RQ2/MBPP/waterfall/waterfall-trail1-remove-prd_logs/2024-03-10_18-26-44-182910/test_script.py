def comb_sort(nums):
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of elements")
    if len(nums) <= 1:
        return nums
    
    shrink_factor = 1.3
    min_gap = 1
    
    sorted = False
    gap = len(nums)
    
    while not sorted:
        gap = int(gap / shrink_factor)
        if gap <= min_gap:
            gap = min_gap
            sorted = True
        else:
            sorted = True
            for i in range(len(nums) - gap):
                if nums[i] > nums[i + gap]:
                    nums[i], nums[i + gap] = nums[i + gap], nums[i]
                    sorted = False
    
    return nums
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()