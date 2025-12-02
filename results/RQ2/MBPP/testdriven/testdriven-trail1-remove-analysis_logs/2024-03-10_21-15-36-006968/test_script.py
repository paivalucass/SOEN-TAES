def sub_list(nums1, nums2):
    '''Write a function to subtract two lists element-wise.
    assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]'''
    if len(nums1) != len(nums2):
        return "Error: Input lists must be of the same length"
    
    for i in range(len(nums1)):
        if not isinstance(nums1[i], int) or not isinstance(nums2[i], int):
            return "Error: Input lists must contain only integers"
    
    result = [nums1[i] - nums2[i] for i in range(len(nums1))]
    return result
import unittest

class Test(unittest.TestCase):
    def test_sub_list(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()