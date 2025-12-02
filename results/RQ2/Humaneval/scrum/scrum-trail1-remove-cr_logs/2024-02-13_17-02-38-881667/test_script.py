def smallest_change(arr):
    length = len(arr)
    changes = 0
    for i in range(length // 2):
        if arr[i] != arr[length - 1 - i]:
            changes += 1
    return changes

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Valid Input Array",
      "Input Data": "arr=[1,2,3,5,4,7,9,6]",
      "Expected Output": "4"
    },
    {
      "Test Title": "Single Element Array",
      "Input Data": "arr=[3]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Empty Input Array",
      "Input Data": "arr=[]",
      "Expected Output": "0"
    },
    {
      "Test Title": "Large Input Array",
      "Input Data": "arr=[10,20,30,40,50,60,70,80,90,100,110,120]",
      "Expected Output": "6"
    },
    {
      "Test Title": "Negative Number in Array",
      "Input Data": "arr=[-1,2,3,5,4,7,9,6]",
      "Expected Output": "4"
    },
    {
      "Test Title": "Duplicate Numbers in Array",
      "Input Data": "arr=[1,2,2,5,4,5,9,6]",
      "Expected Output": "4"
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