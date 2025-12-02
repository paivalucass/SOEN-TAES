def max_occurrences(nums):
    '''Write a function to find the item with maximum frequency in a given list'''
    if not nums:
        return 'Input list is empty'
    
    frequency = defaultdict(int)
    
    for num in nums:
        frequency[num] += 1
    
    max_freq = max(frequency.values())
    max_items = [item for item, freq in frequency.items() if freq == max_freq]
    
    if len(max_items) > 1:
        # Handle tie-breaker scenarios
        return min(max_items)  # Return the smallest item in case of tie
    else:
        return max_items[0]

# Additional test cases
def test_max_occurrences():
    assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == 2  # Test case with multiple items and tie-breaker
    assert max_occurrences([1]) == 1  # List with only one item
    assert max_occurrences([]) == 'Input list is empty'  # Empty list error handling

test_max_occurrences()

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]), 2)

if __name__ == '__main__':
    unittest.main()