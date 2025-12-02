def count_same_pair(nums1, nums2):
    count = sum(1 for a, b in zip(nums1, nums2) if a == b)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9]), 4)

if __name__ == '__main__':
    unittest.main()