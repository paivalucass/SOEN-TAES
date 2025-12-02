def large_product(nums1, nums2, N):
    products = [num1 * num2 for num1 in nums1 for num2 in nums2]
    products.sort(reverse=True)
    return products[:N]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()