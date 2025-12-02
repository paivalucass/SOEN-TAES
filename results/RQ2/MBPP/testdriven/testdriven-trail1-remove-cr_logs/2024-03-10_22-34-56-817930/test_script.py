def intersection_array(array_nums1, array_nums2):
    result = []
    num_set = set(array_nums1)
    for num in array_nums2:
        if num in num_set:
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]), [1, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()