def sub_list(nums1, nums2):
    if not nums1 or not nums2:
        raise ValueError("Input lists cannot be empty")

    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")

    if not all(isinstance(x, (int, float)) for x in nums1) or not all(isinstance(x, (int, float)) for x in nums2):
        raise TypeError("Input lists must contain only numbers")

    result = [x - y for x, y in zip(nums1, nums2)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3],[4,5,6]), [-3,-3,-3])

if __name__ == '__main__':
    unittest.main()