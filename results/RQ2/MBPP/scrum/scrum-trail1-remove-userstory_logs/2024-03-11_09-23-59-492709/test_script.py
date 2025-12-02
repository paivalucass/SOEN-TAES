def sum_Of_Subarray_Prod(arr):
    result = 0
    for i in range(len(arr)):
        product = 1
        for j in range(i, len(arr)):
            product *= arr[j]
            result += product
    return result

# Test Cases:
{
  "requirement analysis": "analysis",
  "test_cases": [
    {
      "Test Title": "Empty input list",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "List with a single element",
      "Input Data": "arr=[5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "List with positive and negative integers",
      "Input Data": "arr=[-3, 2, 5, -7]",
      "Expected Output": "-218"
    },
    {
      "Test Title": "List with a large number of elements",
      "Input Data": "arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
      "Expected Output": "154440"
    },
    {
      "Test Title": "List with zero as an element",
      "Input Data": "arr=[1, 0, 2]",
      "Expected Output": "14"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_Of_Subarray_Prod([1,2,3]), 20)

if __name__ == '__main__':
    unittest.main()