def sub_list(nums1, nums2):
    result = []
    if len(nums1) != len(nums2):
        return None  # Lists of different lengths
    for i in range(len(nums1)):
        if not (isinstance(nums1[i], (int, float)) and isinstance(nums2[i], (int, float))):
            return None  # Non-numeric elements should raise an error
        result.append(nums1[i] - nums2[i])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()