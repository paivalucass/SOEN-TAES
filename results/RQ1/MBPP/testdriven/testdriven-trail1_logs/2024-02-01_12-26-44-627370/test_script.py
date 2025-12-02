def sub_list(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")

    result = [a - b for a, b in zip(nums1, nums2)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()