def right_insertion(a, x):
    '''Write a function to locate the right insertion point for a specified value in sorted order.'''
    
    if len(a) == 0 or x > a[-1]:
        return len(a)
    
    for i in range(len(a)):
        if x <= a[i]:
            return i

    return 0 # If x is smaller than all the values in the input list

# Test cases
assert right_insertion([1,2,4,5],6) == 4
assert right_insertion([1,2,4,5],0) == 0 # If the specified value is smaller than all the values in the input list
assert right_insertion([],6) == 0 # If the input list is empty
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()