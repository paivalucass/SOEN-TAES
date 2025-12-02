def find_First_Missing(array, start=0, end=None):
    '''
    Write a python function to find the smallest missing number from a sorted list of natural numbers.
    assert find_First_Missing([0,1,2,3]) == 4
    '''
    if end is None:
        end = len(array) - 1

    if any(i < 0 or not isinstance(i, int) for i in array):
        raise ValueError("Input list must be sorted and contain only natural numbers")
    
    if not array:
        raise ValueError("Input list cannot be empty")
    
    # Binary search algorithm implementation
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == mid:
            start = mid + 1
        else:
            end = mid - 1
    return start
import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()