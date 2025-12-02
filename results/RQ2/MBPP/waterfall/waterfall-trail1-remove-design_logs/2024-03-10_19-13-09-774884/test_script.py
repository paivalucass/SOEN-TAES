def large_product(nums1, nums2, N):
    if not nums1 or not nums2:
        return []

    products = []
    for i in nums1:
        for j in nums2:
            products.append(i * j)

    products.sort(reverse=True)
    return products[:N]
import unittest

class Test(unittest.TestCase):
    def test_large_product(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()