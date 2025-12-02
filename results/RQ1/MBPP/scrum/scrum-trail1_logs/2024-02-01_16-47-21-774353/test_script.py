def find_min_diff(arr,n):
    arr.sort()
    min_diff = float('inf')
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) < min_diff:
            min_diff = abs(arr[i] - arr[i+1])
    return min_diff

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Array",
      "Input Data": "arr=[1,5,3,19,18,25], n=6",
      "Expected Output": "1"
    },
    {
      "Test Title": "Empty Input Array",
      "Input Data": "arr=[], n=0",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Single Element",
      "Input Data": "arr=[5], n=1",
      "Expected Output": "0"
    },
    {
      "Test Title": "Array with Duplicate Elements",
      "Input Data": "arr=[3,5,3,8], n=4",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25], 6), 1)

if __name__ == '__main__':
    unittest.main()