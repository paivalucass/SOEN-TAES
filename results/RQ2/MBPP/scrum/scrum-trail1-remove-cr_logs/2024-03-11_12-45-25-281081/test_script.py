def max_occurrences(nums):
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_freq_item = None
    max_freq = 0
    for key, value in frequency.items():
        if value > max_freq:
            max_freq = value
            max_freq_item = key
        elif value == max_freq and key != max_freq_item:
            max_freq_item = None
            break
    
    return max_freq_item
import unittest

class Test(unittest.TestCase):
    def test_max_occurrences(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()