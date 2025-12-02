def div_list(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must be of the same length")

    if 0 in nums2:
        raise ValueError("Cannot divide by zero in nums2")

    return [nums1[i] / nums2[i] if nums2[i] != 0 else "Error: Division by zero" for i in range(len(nums1))]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()