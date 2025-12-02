def div_list(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        raise ValueError("Input lists cannot be empty")
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")
    
    result = []
    for i in range(len(nums1)):
        if nums2[i] == 0:
            raise ValueError("Division by zero is not allowed")
        result.append(nums1[i] / nums2[i])
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()