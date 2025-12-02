def sub_list(nums1, nums2):
    if len(nums1) != len(nums2):
        return "Error: Arrays are of different lengths"
    
    result = [num1 - num2 for num1, num2 in zip(nums1, nums2)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sub_list([1, 2, 3], [4, 5, 6]), [-3, -3, -3])

if __name__ == '__main__':
    unittest.main()