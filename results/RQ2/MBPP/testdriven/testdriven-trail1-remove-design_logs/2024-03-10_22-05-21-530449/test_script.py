def large_product(nums1, nums2, N):
    import heapq
    if N <= 0:
        return "Invalid Input for N. N must be a positive integer."
    h = []
    for x in nums1:
        for y in nums2:
            product = x * y
            if len(h) < N:
                heapq.heappush(h, product)
            else:
                if product > h[0]:
                    heapq.heappop(h)
                    heapq.heappush(h, product)
    return sorted(h, reverse=True)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3), [60, 54, 50])

if __name__ == '__main__':
    unittest.main()