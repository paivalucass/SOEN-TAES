def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    for n1 in nums1:
        for n2 in nums2:
            if len(pairs) < k:
                pairs.append([n1, n2])
            else:
                max_sum_pair = max(pairs, key=lambda x: x[0] + x[1])
                if n1 + n2 < max_sum_pair[0] + max_sum_pair[1]:
                    pairs.remove(max_sum_pair)
                    pairs.append([n1, n2])
    return pairs
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()