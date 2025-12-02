def k_smallest_pairs(nums1, nums2, k):
    if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0 or len(nums1) != len(nums2):
        raise ValueError("Invalid input: nums1 and nums2 must be non-empty arrays of the same length.")

    if k > len(nums1) * len(nums2):
        raise ValueError("Invalid input: k cannot be greater than the total number of pairs that can be formed from nums1 and nums2.")

    pairs = []
    for n1 in nums1:
        for n2 in nums2:
            pairs.append([n1, n2])

    pairs.sort(key=sum)
    return pairs[:k]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()