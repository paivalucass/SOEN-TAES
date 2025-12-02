def max_occurrences(nums):
    from collections import defaultdict
    freq_dict = defaultdict(int)
    for num in nums:
        freq_dict[num] += 1
    max_freq_item = max(freq_dict, key=freq_dict.get)
    return max_freq_item
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()