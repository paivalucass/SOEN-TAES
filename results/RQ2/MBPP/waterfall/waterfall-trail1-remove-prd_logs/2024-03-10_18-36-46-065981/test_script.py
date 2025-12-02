import heapq

def k_smallest_pairs(nums1, nums2, k):
    heap = []
    for n1 in nums1:
        for n2 in nums2:
            if len(heap) < k:
                heapq.heappush(heap, (n1 + n2, [n1, n2]))
            else:
                if n1 + n2 < heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (n1 + n2, [n1, n2]))
                else:
                    break
    return [pair[1] for pair in heap]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()