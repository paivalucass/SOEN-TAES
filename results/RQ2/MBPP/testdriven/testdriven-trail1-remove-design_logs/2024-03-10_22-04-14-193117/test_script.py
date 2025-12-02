def sub_list(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("Error: Lists must be of the same length")
    return [x - y for x, y in zip(nums1, nums2)]
import unittest

class Test(unittest.TestCase):
    def test_sub_list(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()