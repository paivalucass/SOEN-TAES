def div_list(nums1, nums2):
    if not nums2:
        raise ValueError("Error: nums2 is empty")

    if len(nums1) != len(nums2):
        raise ValueError("Error: Division between lists of different lengths is not well-defined")

    result = []
    for i in range(len(nums1)):
        if nums2[i] == 0:
            raise ValueError("Error: Division by zero")
        result.append(nums1[i] / nums2[i])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()