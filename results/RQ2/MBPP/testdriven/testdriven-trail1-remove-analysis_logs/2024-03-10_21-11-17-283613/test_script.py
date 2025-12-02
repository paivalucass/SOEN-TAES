def max_occurrences(nums):
    '''
    Write a function to find the item with maximum frequency in a given list.
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2])==2
    '''
    if not isinstance(nums, list):
        return "Input is not a list"
    
    if len(nums) == 0:
        return None
    
    if len(nums) == 1:
        return nums[0]
    
    if all(isinstance(x, int) for x in nums):
        from collections import Counter
        counts = Counter(nums)
        max_count = max(counts.values())
        max_items = [k for k, v in counts.items() if v == max_count]
        return min(max_items)
    else:
        return "List contains non-integer elements"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()