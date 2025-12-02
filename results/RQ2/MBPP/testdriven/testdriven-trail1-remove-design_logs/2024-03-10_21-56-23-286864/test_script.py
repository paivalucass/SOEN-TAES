def comb_sort(nums):
    '''Write a function to sort a list of elements.'''
    gap = len(nums)
    shrink_factor = 1.3
    swapped = True
    
    while gap > 1 or swapped:
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1
        
        swapped = False
        for i in range(len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
    
    return nums

assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()