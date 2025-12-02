def div_list(nums1, nums2):
    if len(nums1) != len(nums2):
        return "Error: Lists have different lengths"

    if not all(isinstance(x, (int, float)) for x in nums1) or not all(isinstance(x, (int, float)) for x in nums2):
        return "Error: nums1 and nums2 must contain only numeric values"

    if not nums1 or not nums2:
        return "Error: nums1 and nums2 must not be empty"

    results = []
    for num1, num2 in zip(nums1, nums2):
        if num2 == 0:
            return "Error: Division by zero"
        else:
            results.append(num1 / num2)

    return results
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4,5,6],[1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()