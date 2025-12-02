def div_list(nums1, nums2):
    if any(num == 0 for num in nums2):
        raise ValueError("Error: Division by zero is not allowed")
    if len(nums1) != len(nums2):
        raise ValueError("Error: Input lists must have the same length")
    
    return [num1 / num2 for num1, num2 in zip(nums1, nums2)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()