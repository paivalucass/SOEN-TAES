def right_insertion(a, x):
    '''Write a function to locate the right insertion point for a specified value in sorted order.
    Inputs:
        a: sorted list of integers
        x: value to be inserted
    Output:
        index where 'x' should be inserted to maintain the sorted order of the list
    '''
    # Implementation details:
    # - Iterate through the sorted list 'a' and compare each element with 'x' to find the correct insertion point
    # - Use binary search for efficient implementation
    # - Handle edge cases like an empty list, single element list, and multiple element list for testing purposes
    
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        if x > a[0]:
            return 1
        else:
            return 0
    else:
        left = 0
        right = len(a) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5],6), 4)

if __name__ == '__main__':
    unittest.main()