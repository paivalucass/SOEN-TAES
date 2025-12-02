def div_list(nums1, nums2):
    if not isinstance(nums1, list) or not isinstance(nums2, list):
        return "Error: Inputs are not lists"
    if len(nums1) == 0 and len(nums2) == 0:
        return "Error: Both input lists are empty"

    if len(nums1) != len(nums2):
        return "Error: Lists are of different lengths"

    for i in range(len(nums1)):
        if not (isinstance(nums1[i], (int, float)) and isinstance(nums2[i], (int, float))):
            return "Error: Non-numeric values are present in the lists"

    try:
        result = [nums1[i] / nums2[i] for i in range(len(nums1))]
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
import unittest

class Test(unittest.TestCase):
    def test_div_list(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()