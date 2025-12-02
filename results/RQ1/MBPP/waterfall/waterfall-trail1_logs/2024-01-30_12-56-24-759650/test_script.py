def sub_list(nums1, nums2):
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise ValueError("Input must be lists")
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")
    if len(nums1) == 0 or len(nums2) == 0:
        raise ValueError("Input lists cannot be empty")
    result = []
    for i in range(len(nums1)):
        result.append(nums1[i] - nums2[i])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()