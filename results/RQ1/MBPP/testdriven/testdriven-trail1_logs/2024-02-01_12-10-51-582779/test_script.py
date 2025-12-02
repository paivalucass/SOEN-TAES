def max_Abs_Diff(arr):
    '''Write a python function to find the maximum absolute difference between any two elements in a given array.
    assert max_Abs_Diff((2,1,5,3)) == 4'''
    
    if len(arr) < 2:
        return 0
    
    max_val = max(arr)
    min_val = min(arr)
    return abs(max_val - min_val)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()