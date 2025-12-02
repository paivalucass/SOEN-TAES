def count_same_pair(nums1, nums2):
    '''
    The input is defined as two lists of the same length. Write a function to count indices where the lists have the same values.
    assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4
    '''
    if not nums1 or not nums2 or len(nums1) != len(nums2):
        return -1
    
    same_count = 0
    for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
            same_count += 1
    
    return same_count
import unittest

class Test(unittest.TestCase):
    def test_count_same_pair(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9]), 4)

if __name__ == '__main__':
    unittest.main()