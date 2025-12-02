def k_smallest_pairs(nums1, nums2, k):
    import heapq
    if not nums1 or not nums2 or k <= 0:
        return []
    
    result = []
    min_heap = []
    
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heapq.heappush(min_heap, (nums1[i], nums2[j]))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0] + min_heap[0][1]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (nums1[i], nums2[j]))
    
    result = [list(pair) for pair in min_heap]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()