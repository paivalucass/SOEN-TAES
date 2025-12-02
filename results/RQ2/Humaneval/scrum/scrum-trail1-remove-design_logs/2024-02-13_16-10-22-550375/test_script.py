def smallest_change(arr):
    # Given an array arr of integers, find the minimum number of elements that
    # need to be changed to make the array palindromic. A palindromic array is an array that
    # is read the same backwards and forwards. In one change, you can change one element to any other element.
    
    n = len(arr)
    count = 0
    
    for i in range(n//2):
        if arr[i] != arr[n-1-i]:
            count += 1
    
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Test for array with odd length",
      "Input Data": "arr=[1,2,3,5,4,7,9,6]",
      "Expected Output": "4"
    },
    {
      "Test Title": "Test for array with even length",
      "Input Data": "arr=[1, 2, 3, 4, 3, 2, 2]",
      "Expected Output": "1"
    },
    {
      "Test Title": "Test for palindromic array",
      "Input Data": "arr=[1, 2, 3, 2, 1]",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()