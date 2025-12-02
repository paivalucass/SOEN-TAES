def can_arrange(arr):
    """
    Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    
    breakIndex = -1
    
    if len(arr) <= 1:
        return breakIndex
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            breakIndex = i
    
    return breakIndex
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)

    def test2(self):
        self.assertEqual(can_arrange([1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()