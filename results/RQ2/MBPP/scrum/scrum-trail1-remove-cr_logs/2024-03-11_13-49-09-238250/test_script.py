def div_list(nums1, nums2):
    result = []
    if len(nums1) != len(nums2):
        return "Error: Invalid Input"
    for i in range(len(nums1)):
        if not (isinstance(nums1[i], (int, float)) and isinstance(nums2[i], (int, float))):
            return "Error: Invalid Input"
        result.append(nums1[i] / nums2[i])
    return result
import unittest

class Test(unittest.TestCase):
    def test_div_list(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()