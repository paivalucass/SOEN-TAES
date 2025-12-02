def large_product(nums1, nums2, N):
    if not nums1 or not nums2:
        return "Error: nums1 and nums2 must be non-empty lists"
    if N <= 0:
        return "Error: N must be a positive integer"

    products = []
    for num1 in nums1:
        for num2 in nums2:
            products.append(num1 * num2)
    products.sort(reverse=True)
    if N > len(products):
        return "Error: N cannot be larger than possible products"
    return products[:N]
import unittest

class Test(unittest.TestCase):
    def test_large_product(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()