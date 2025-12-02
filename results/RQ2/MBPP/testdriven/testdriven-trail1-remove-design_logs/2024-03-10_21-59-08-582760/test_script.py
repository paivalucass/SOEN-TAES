def max_occurrences(nums):
    if not nums:
        return None
    else:
        freq_dict = {}
        max_freq_item = None
        max_freq = 0
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
            if freq_dict[num] > max_freq:
                max_freq = freq_dict[num]
                max_freq_item = num
            elif freq_dict[num] == max_freq and num < max_freq_item:
                max_freq_item = num
        return max_freq_item
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()