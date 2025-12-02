def max_occurrences(nums):
    from collections import Counter
    
    if not nums:
        return "Error Handling"

    count = Counter(nums)
    max_freq = max(count.values())
    max_items = [key for key, value in count.items() if value == max_freq]

    if len(max_items) == 1:
        return max_items[0]
    else:
        return "Error Handling"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()