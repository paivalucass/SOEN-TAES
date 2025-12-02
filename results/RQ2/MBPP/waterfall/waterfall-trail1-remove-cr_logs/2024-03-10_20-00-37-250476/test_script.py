def get_Inv_Count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Empty Array Test",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "No Inversions Test",
      "Input Data": "arr=[1, 2, 3, 4, 5]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Multiple Inversions Test",
      "Input Data": "arr=[5, 4, 3, 2, 1]",
      "Expected Output": "10"
    },
    {
      "Test Title": "Boundary Condition Test",
      "Input Data": "arr=[1, 20, 6, 4, 5]",
      "Expected Output": "5"
    },
    {
      "Test Title": "Large Array Test",
      "Input Data": "arr=[1000000, 999999, ..., 1]",
      "Expected Output": "499999500000"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_Inv_Count([1,20,6,4,5]), 5)

if __name__ == '__main__':
    unittest.main()