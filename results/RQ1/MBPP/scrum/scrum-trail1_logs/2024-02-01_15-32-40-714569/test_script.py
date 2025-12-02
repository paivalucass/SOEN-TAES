def k_smallest_pairs(nums1, nums2, k):
    pairs = []
    for num1 in nums1:
        for num2 in nums2:
            pairs.append([num1, num2])
    pairs.sort(key=sum)
    return pairs[:k]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(k_smallest_pairs([1,3,7],[2,4,6],2), [[1, 2], [1, 4]])

if __name__ == '__main__':
    unittest.main()