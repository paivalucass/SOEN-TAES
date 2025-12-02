import heapq

def large_product(nums1, nums2, N):
    if not nums1 or not nums2:
        return []

    products = [num1 * num2 for num1 in nums1 for num2 in nums2]
    largest_products = heapq.nlargest(N, products)
    return largest_products
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()