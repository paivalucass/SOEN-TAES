def odd_length_sum(arr):
    result = 0
    n = len(arr)
    for i in range(n):
        for j in range(i, n, 2):
            for k in range(i, j+1):
                result += arr[k]
    return result

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Input array contains only one element",
      "Input Data": "arr=[1]",
      "Expected Output": "1"
    },
    {
      "Test Title": "Input array contains negative numbers",
      "Input Data": "arr=[-1,2,-3,4]",
      "Expected Output": "6"
    },
    {
      "Test Title": "Large input arrays",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10]",
      "Expected Output": "144"
    },
    {
      "Test Title": "Input validation",
      "Input Data": "arr=['a','b','c']",
      "Expected Output": "0"
    },
    {
      "Test Title": "Empty input array",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_length_sum([1,2,4]), 14)

if __name__ == '__main__':
    unittest.main()