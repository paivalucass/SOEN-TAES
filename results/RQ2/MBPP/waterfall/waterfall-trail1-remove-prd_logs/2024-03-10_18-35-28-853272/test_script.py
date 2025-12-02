def large_product(nums1, nums2, N):
    products = []
    nums1.sort()
    nums2.sort()
    for i in range(N):
        products.append(nums1[-i-1] * nums2[-i-1])
    products.sort(reverse=True)
    return products
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()