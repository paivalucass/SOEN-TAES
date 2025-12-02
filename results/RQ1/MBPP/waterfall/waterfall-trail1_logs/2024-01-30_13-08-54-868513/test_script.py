import heapq

def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2:
        raise ValueError("Input arrays cannot be empty")

    if k <= 0 or k > len(nums1) * len(nums2):
        raise ValueError("Invalid value of k")

    if k == 0:
        return []

    result = []
    min_heap = []

    for n1 in nums1:
        for n2 in nums2:
            pair_sum = n1 + n2
            if len(min_heap) < k:
                heapq.heappush(min_heap, (pair_sum, [n1, n2]))
            else:
                if pair_sum < min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (pair_sum, [n1, n2]))

    for _ in range(k):
        if min_heap:
            _, pair = heapq.heappop(min_heap)
            result.append(pair)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()