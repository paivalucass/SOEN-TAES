from typing import List

def div_list(nums1: List[int], nums2: List[int]) -> List[float]:
    if len(nums1) != len(nums2):
        raise ValueError("Input lists should have the same length")

    result = []
    for i in range(len(nums1)):
        if nums2[i] == 0:
            raise ValueError("Division by zero error")
        result.append(nums1[i] / nums2[i])

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(div_list([4, 5, 6], [1, 2, 3]), [4.0, 2.5, 2.0])

if __name__ == '__main__':
    unittest.main()