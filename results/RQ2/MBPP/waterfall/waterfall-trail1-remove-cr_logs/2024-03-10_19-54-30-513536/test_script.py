def max_occurrences(nums):
    if not nums:
        return None

    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    max_freq = max(frequency_map.values())
    max_freq_items = [item for item, freq in frequency_map.items() if freq == max_freq]

    if len(max_freq_items) > 1:
        return max_freq_items

    return max_freq_items[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()