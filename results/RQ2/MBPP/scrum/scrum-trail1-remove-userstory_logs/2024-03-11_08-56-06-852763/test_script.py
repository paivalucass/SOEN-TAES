def max_occurrences(nums):
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    max_freq = 0
    max_item = None
    for item, freq in freq_map.items():
        if freq > max_freq:
            max_freq = freq
            max_item = item
    
    return max_item
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()