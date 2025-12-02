def k_smallest_pairs(nums1, nums2, k):
    import heapq

    nums1.sort()
    nums2.sort()

    result = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(result) < k:
                heapq.heappush(result, (nums1[i], nums2[j]))
            else:
                if nums1[i] + nums2[j] < result[0][0] + result[0][1]:
                    heapq.heappop(result)
                    heapq.heappush(result, (nums1[i], nums2[j]))
                else:
                    break

    output = []
    for pair in result:
        output.append(list(pair))

    return output
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()