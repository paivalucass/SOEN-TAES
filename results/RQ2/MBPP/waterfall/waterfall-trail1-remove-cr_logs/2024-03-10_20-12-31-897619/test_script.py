def div_list(nums1,nums2):
    result = []
    if len(nums1) == 0 or len(nums2) == 0:
        return "Error: Empty input lists"
    for x, y in zip(nums1, nums2):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            return "Error: Non-numeric elements in input lists"
        elif y == 0:
            return "Error: Division by zero"
        else:
            result.append(x / y)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()