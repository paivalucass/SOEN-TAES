def intersection_array(array_nums1, array_nums2):
    '''Write a function to find the intersection of two arrays.'''
    if not array_nums1 or not array_nums2:
        return []  # handle empty or null input arrays
    
    # Use Python built-in set() function to find the intersection of two arrays
    intersection = list(set(array_nums1) & set(array_nums2))
    
    return sorted(intersection)

assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]), [1, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()