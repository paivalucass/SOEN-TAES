def find_unique_number(arr):
    # This function finds the unique number in an array
    # If the array has an odd number of elements, it returns the unique number
    # If the array has an even number of elements, it returns None
    
    for index in range(0, len(arr), 2):
        if index == len(arr) - 1:
            return arr[index]
        if arr[index] != arr[index + 1]:
            return arr[index]
    return None

def search(arr):
    # This function finds the element that appears only once in a sorted array
    # If there is no unique element, it returns None
    
    for index in range(0, len(arr), 2):
        if index == len(arr) - 1:
            return arr[index]
        if arr[index] != arr[index + 1]:
            return arr[index]
    return None

# Test Cases:
{
  "test_cases": [
    {
      "TestTitle": "Single unique element in array",
      "InputData": "arr=[1,1,2,2,3]",
      "ExpectedOutput": "3"
    },
    {
      "TestTitle": "Empty array",
      "InputData": "arr=[]",
      "ExpectedOutput": "None"
    },
    {
      "TestTitle": "No unique element in array",
      "InputData": "arr=[1,1,2,2,3,3]",
      "ExpectedOutput": "None"
    }
  ]
}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()