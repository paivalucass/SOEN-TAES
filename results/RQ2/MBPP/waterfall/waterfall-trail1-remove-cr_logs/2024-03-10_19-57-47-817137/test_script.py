def intersection_array(array_nums1, array_nums2):
    set1 = set(array_nums1)
    set2 = set(array_nums2)
    result = []
    for num in set1:
        if num in set2:
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9]), [1, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()