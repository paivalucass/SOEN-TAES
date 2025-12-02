def sub_list(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("The lists must have the same length for element-wise subtraction.")

    result = [nums1[i] - nums2[i] for i in range(len(nums1))]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()