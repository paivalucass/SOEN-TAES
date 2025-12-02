def get_pairs_count(arr, sum):
    pairs_count = 0
    hashMap = {}
    for num in arr:
        complement = sum - num
        if complement in hashMap:
            pairs_count += hashMap[complement]
        if num in hashMap:
            hashMap[num] += 1
        else:
            hashMap[num] = 1
    return pairs_count
import unittest

class TestPairsCount(unittest.TestCase):
    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1,1,1,1],2), 6)

if __name__ == '__main__':
    unittest.main()