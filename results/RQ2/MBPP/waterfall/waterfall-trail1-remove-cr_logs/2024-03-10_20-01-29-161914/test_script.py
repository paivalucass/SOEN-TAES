def large_product(nums1, nums2, N):
    if not isinstance(nums1, list) or not isinstance(nums2, list) or not isinstance(N, int):
        raise TypeError("Input parameters should be of type list and integer")

    if len(nums1) == 0 or len(nums2) == 0 or N > len(nums1) * len(nums2):
        raise ValueError("Input lists cannot be empty and N should not be larger than the length of both input lists")

    products = [x * y for x in nums1 for y in nums2]
    products.sort(reverse=True)

    return products[:N]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()