def right_insertion(sorted_list, value):
    # Initialize the start and end pointers for binary search
    start = 0
    end = len(sorted_list) - 1
    
    # Handle the case where the list is empty
    if len(sorted_list) == 0:
        return 0
    
    # Handle the case where the value is greater than all elements
    if value > sorted_list[-1]:
        return len(sorted_list)
    
    # Binary search to find the right insertion point
    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] <= value:
            start = mid + 1
        else:
            end = mid - 1
            
    return start
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()