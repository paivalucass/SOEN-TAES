def smallest_change(arr):
    if arr == arr[::-1]:
        return 0
    else:
        changes = 0
        for i in range(len(arr)//2):
            if arr[i] != arr[-i-1]:
                changes += 1
        return changes

# Test Cases:
{
  "test_cases": [
    {
      "Test Title": "Array with odd length",
      "Input Data": "arr=[1,2,3,5,4,7,9,6]",
      "Expected Output": 4
    },
    {
      "Test Title": "Array with even length",
      "Input Data": "arr=[1,2,3,4,3,2,2]",
      "Expected Output": 1
    },
    {
      "Test Title": "Palindrome array",
      "Input Data": "arr=[1,2,3,2,1]",
      "Expected Output": 0
    },
    {
      "Test Title": "Empty array",
      "Input Data": "arr=[]",
      "Expected Output": 0
    },
    {
      "Test Title": "Array with negative numbers",
      "Input Data": "arr=[-1,-2,-3,-4]",
      "Expected Output": 4
    },
    {
      "Test Title": "Array with all same elements",
      "Input Data": "arr=[1,1,1,1,1]",
      "Expected Output": 0
    },
    {
      "Test Title": "Array with large number of elements",
      "Input Data": "arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]",
      "Expected Output": 25
    },
    {
      "Test Title": "Non-array input",
      "Input Data": "arr='not an array'",
      "Expected Output": 0
    },
    {
      "Test Title": "Array with non-numeric elements",
      "Input Data": "arr=['a','b','c']",
      "Expected Output": 0
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