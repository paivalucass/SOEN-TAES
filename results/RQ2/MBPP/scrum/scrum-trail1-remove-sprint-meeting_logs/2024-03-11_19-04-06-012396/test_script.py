def count_same_pair(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")
    
    count = sum(1 for i in range(len(nums1)) if nums1[i] == nums2[i])
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]), 4)

if __name__ == '__main__':
    unittest.main()