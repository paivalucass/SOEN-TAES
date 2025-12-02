def big_sum(nums):
    import heapq
    if not nums:
        return 0
    min_heap = []
    max_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, -num)
    return -heapq.heappop(max_heap) + heapq.heappop(min_heap)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(big_sum([1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()