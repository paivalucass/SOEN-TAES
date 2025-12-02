def get_Inv_Count(arr):
    inv_count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count
# Test Cases:
{
  "requirement analysis": "The python function should efficiently count inversions in an array using a divide and conquer approach like merge sort",
  "test_cases": [
    {
      "Test Title": "Valid input array",
      "Input Data": "parameter1=[1,20,6,4,5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Empty input array",
      "Input Data": "parameter1=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input array with single element",
      "Input Data": "parameter1=[1]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input array with no inversions",
      "Input Data": "parameter1=[1,2,3,4,5]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input array with large elements",
      "Input Data": "parameter1=[1000, 2000, 3000, 4000, 5000]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Input array with all elements in descending order",
      "Input Data": "parameter1=[5, 4, 3, 2, 1]",
      "Expected Output": "10"
    },
    {
      "Test Title": "Input array with negative numbers",
      "Input Data": "parameter1=[-1, -2, -3, -4, -5]",
      "Expected Output": "10"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1,20,6,4,5]), 5)

if __name__ == '__main__':
    unittest.main()