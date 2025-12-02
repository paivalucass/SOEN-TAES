def div_list(nums1, nums2):
    try:
        if not isinstance(nums1, list) or not isinstance(nums2, list):
            raise TypeError("error: input parameters are not lists")
        if len(nums1) == 0 or len(nums2) == 0:
            raise ValueError("error: input lists are empty")
        if len(nums1) != len(nums2):
            raise ValueError("error: lists are of unequal length")
        
        result = []
        for i in range(len(nums1)):
            if nums2[i] == 0:
                raise ZeroDivisionError("error: division by zero")
            result.append(nums1[i] / nums2[i])
        
        return result
    except (TypeError, ValueError, ZeroDivisionError) as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()