def div_list(nums1, nums2):
    if len(nums1) != len(nums2):
        raise ValueError("Input lists must have the same length")
    if 0 in nums2:
        raise ValueError("Divisor list cannot contain zero values")

    result = []
    for num1, num2 in zip(nums1, nums2):
        try:
            result.append(num1 / num2)
        except ZeroDivisionError:
            result.append(float('inf'))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()