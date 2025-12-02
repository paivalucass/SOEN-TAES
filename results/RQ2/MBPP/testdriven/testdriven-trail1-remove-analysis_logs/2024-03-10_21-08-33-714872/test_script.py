def comb_sort(nums):
    '''Write a function to sort a list of elements.
    assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]'''

    gap = len(nums)
    shrink_factor = 1.3
    is_swapped = True
    
    while gap > 1 or is_swapped:
        gap = int(gap / shrink_factor)
        if gap < 1:
            gap = 1
        
        i = 0
        is_swapped = False
        while i + gap < len(nums):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i] # swap the elements
                is_swapped = True
            i += 1
    
    return nums
import unittest

class Test(unittest.TestCase):
    def test_comb_sort(self):
        self.assertEqual(comb_sort([5, 15, 37, 25, 79]), [5, 15, 25, 37, 79])

if __name__ == '__main__':
    unittest.main()