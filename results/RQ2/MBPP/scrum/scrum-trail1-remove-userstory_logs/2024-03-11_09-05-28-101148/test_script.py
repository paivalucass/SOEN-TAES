def sub_list(nums1, nums2):
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        raise TypeError("Input is not a list")
    if len(nums1) != len(nums2):
        raise ValueError("Lists are not of the same length")
    
    result = [a - b for a, b in zip(nums1, nums2)]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()