def find_min_diff(arr, n):
    '''This function calculates the minimum difference between any two elements in a given array'''

    # Input validation
    if len(arr) < 2:
        return "Array should have at least 2 elements"
    if n < 2:
        return "n should be at least 2"

    arr.sort()
    min_diff = float('inf')
    
    # Calculate minimum difference
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25], 6), 1)

if __name__ == '__main__':
    unittest.main()