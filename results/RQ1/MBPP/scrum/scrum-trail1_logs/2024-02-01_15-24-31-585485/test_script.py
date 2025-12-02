def large_product(nums1, nums2, N):
    product_list = [x * y for x in nums1 for y in nums2]
    product_list.sort(reverse=True)
    return product_list[:N]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()