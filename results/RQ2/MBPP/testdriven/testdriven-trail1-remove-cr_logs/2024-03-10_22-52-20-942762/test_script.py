def find_min_diff(arr, n):
    # Write a python function to find the minimum difference between any two elements in a given array
    # https://www.geeksforgeeks.org/find-minimum-difference-pair/
  
    min_diff = float('inf')
    arr.sort()
    
    for i in range(n-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
  
    return min_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25],6), 1)

if __name__ == '__main__':
    unittest.main()