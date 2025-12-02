def intersection_array(array_nums1, array_nums2):
    return sorted(list(set(array_nums1) & set(array_nums2)))
import unittest

class Test(unittest.TestCase):
    def test_intersection_array(self):
        self.assertEqual(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]), [1, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()