def merge_sorted_list(num1, num2, num3):
    '''Write a function to merge three lists into a single sorted list.'''
    import heapq
    
    # Error handling for empty input lists or non-numeric elements
    for l in [num1, num2, num3]:
        if not l:
            return []
        for element in l:
            if not isinstance(element, (int, float)):
                raise ValueError("Input lists should only contain numeric elements")
    
    # Merge the lists efficiently using heapq merge function
    merged_list = sorted(heapq.merge(num1, num2, num3))
    
    return merged_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge_sorted_list([25, 24, 15, 4, 5, 29, 110], [19, 20, 11, 56, 25, 233, 154], [24, 26, 54, 48]), [4, 5, 11, 15, 19, 20, 24, 24, 25, 25, 26, 29, 48, 54, 56, 110, 154, 233])

if __name__ == '__main__':
    unittest.main()