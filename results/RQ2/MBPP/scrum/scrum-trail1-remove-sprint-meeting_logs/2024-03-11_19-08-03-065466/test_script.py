def find_min_diff(arr, n):
    arr.sort()
    min_diff = float('inf')
    for i in range(n-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid input array with positive integers",
      "Input Data": "arr=[1,5,3,19,18,25], n=6",
      "Expected Output": "1"
    },
    {
      "Test Title": "Valid input array with negative integers",
      "Input Data": "arr=[-3,-5,-1,-8,-10], n=5",
      "Expected Output": "2"
    },
    {
      "Test Title": "Valid input array with duplicate elements",
      "Input Data": "arr=[2,4,6,8,2,10], n=6",
      "Expected Output": "0"
    },
    {
      "Test Title": "Valid input array with single element",
      "Input Data": "arr=[5], n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Invalid input array with empty array",
      "Input Data": "arr=[], n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Invalid input array with null input",
      "Input Data": "arr=null, n=null",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge case: Large input array",
      "Input Data": "arr=[1000000,2000000,3000000], n=3",
      "Expected Output": "1000000"
    },
    {
      "Test Title": "Edge case: Array with maximum value",
      "Input Data": "arr=[2147483647, 2147483647], n=2",
      "Expected Output": "0"
    },
    {
      "Test Title": "Edge case: Array with minimum value",
      "Input Data": "arr=[-2147483648, -2147483648], n=2",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25],6), 1)

if __name__ == '__main__':
    unittest.main()