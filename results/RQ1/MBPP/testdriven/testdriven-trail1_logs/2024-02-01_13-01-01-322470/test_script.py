def split_Arr(l, n):
    '''Write a python function to split a list at the nth element and add the first part to the end.'''
    
    # Check if input list length is less than the specified split index
    if len(l) < n:
        raise ValueError("Split index is greater than the length of the list")

    # Split the list at the nth element and add the first part to the end
    return l[n:] + l[:n]

# Test Cases
assert split_Arr([], 0) == []
assert split_Arr([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 5) == [6,7,8,9,10,11,12,13,14,15,1,2,3,4,5]
assert split_Arr([1,2,3,4,5], -2) == [4,5,1,2,3]
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()