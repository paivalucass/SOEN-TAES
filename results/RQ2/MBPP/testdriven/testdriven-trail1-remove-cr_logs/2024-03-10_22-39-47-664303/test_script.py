import heapq

def k_smallest_pairs(nums1, nums2, k):
    if k <= 0 or not nums1 or not nums2:
        return []

    result = []
    heap = []

    for n1 in nums1:
        for n2 in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (n1 + n2, [n1, n2]))
            else:
                if n1 + n2 < heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (n1 + n2, [n1, n2]))

    for _ in range(min(k, len(heap))):
        result.append(heapq.heappop(heap)[1])

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()