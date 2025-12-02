def max_Abs_Diff(arr):
    # check for empty input array
    if len(arr) == 0:
        return None
    
    # check for single element input array
    if len(arr) == 1:
        return 0
    
    # find maximum and minimum elements in the array
    max_element = max(arr)
    min_element = min(arr)
    
    # calculate the absolute difference between the maximum and minimum elements
    abs_diff = abs(max_element - min_element)
    
    return abs_diff

# validate the output for a specific input array (2,1,5,3)
assert max_Abs_Diff((2,1,5,3)) == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()